/**
 * Reader Book Flip plugin
 * @author Wei.Ge<weix.ge@intel.com>
 * @version 0.1.0
 *
 */
define(function(require, exports, module) {

  'use strict';
  // var FPSmeter = require("pkg!fps");
  // var collector = require("pkg!collector");
  var BookFlip = function(options, element) {

    this.$el = $(element);
    this._init(options);

  };

  var startFlip;

  BookFlip.defaults = {
    speed: 1000,
    item: ".page",
    activePage: 1,
    onend: function(old, page, isLimit) {
      return false;
    },
    onstart: function(page) {
      return false;
    }
  };

  BookFlip.prototype = {
    /**
     * Initialize book class.
     *
     * @param options
     * @private
     */
    _init: function(options) {

      // merge user custom options and defaults object.
      this.options = $.extend(true, {}, BookFlip.defaults, options);

      // change animation speed with stylesheet.
      var speed = this.options.speed;

      if (speed !== undefined && BookFlip.defaults.speed !== this.options.speed) {
        var style = document.createElement("style");
        document.head.appendChild(style);
        style.appendChild(document.createTextNode(''));
        style.sheet.insertRule(this.options.item + ".animation {-webkit-transition-duration:" + this.options.speed + "ms;}", 0);
        console.log(style.sheet.cssRules);
      }


      // set the perspective
      this.$el.css('perspective', this.options.perspective);
      // items
      this.$items = this.$el.children(this.options.item);
      // total items
      this.itemsCount = this.$items.length;
      // current item's index
      this.activePage = this.options.activePage;
      // previous item's index
      this.prevPage = this.activePage - 1;

      // show first item
      this.$items.eq(this.activePage).addClass("active show");
      this.$items.eq(this.prevPage).addClass("show");

      this.transEndEventName = 'webkitTransitionEnd.bookblock';

    },
    /**
     * Do book page flip animation.
     *
     * @param dir  {string} the direction book page flip to .
     * @param page {number} the page number book page neef flip to .
     * @returns {boolean}
     * @private
     */
    _action: function(dir, page) {
      console.time("prepare animation");
      console.timeEnd("click trigger");
      // if the animation is doing now.
      if (this.isAnimating) return false;

      this.isAnimating = true;

      // prev page always equal to the number of previous activation page, whether this.end is true.
      this.prevPage = this.activePage;


      if (page !== undefined && !isNaN(page)) {

        this.activePage = page;

      } else if (dir === "next") {

        if (this.activePage === (this.itemsCount - 1)) {
          this.end = true;
        } else {
          this.activePage += 1;
        }

      } else if (dir === "prev") {

        if (this.activePage === 1) {
          this.end = true;
        } else {
          this.activePage -= 1;
        }

      }

      // callback trigger   1ms - 9ms
      this.options.onstart(this.prevPage, this.activePage);

      if (!dir) throw new Error("You don't give me the direction");

      switch (dir) {
        case "next":
          this._doNext();
          break;
        case "prev":
          this._doPrev();
          break;
        default:
          throw new Error("Your program has a bug.");
          break;
      }
    },
    _doNext: function() {
      var prev = this.prevPage,
        active = this.activePage,
        $prev = this.$items.eq(prev),
        $active = this.$items.eq(active),
        html,
        // prev page left content
        $prevLeft;

      // End animation
      if (this.end) return this._doEnd("next", $prev);


      if (prev + 1 !== active) {
        // copy content of left page to prev page left page;
        $prevLeft = $prev.find(".left-page");
        html = $prevLeft.html();
        $prevLeft.html(this.$items.eq(active - 1).find(".left-page").html());
      }
      if (this.options.speed == 0) {
        $prev.removeClass("active");
        $active.addClass("show active");
        this._doNextEnd($prev, html, $prevLeft);
        return;
      }

      $prev
        .addClass("animation")
        .one(this.transEndEventName, this._doNextEnd.bind(this, $prev, html, $prevLeft));
      console.timeEnd("prepare animation");
      console.time("paint");
      // do flip animation 
      this._async(function() {
        console.timeEnd("paint");
        $prev.removeClass("active");
        $active.addClass("show active");
        console.time("transition");
      }, 20);


    },
    _doNextEnd: function($prev, html, $prevLeft) {
      console.timeEnd("transition");
      console.timeEnd("flip page");
      console.time('render new page');

      

      this._async(function() {
        this._reset();

        // reset prev page;
        $prev.removeClass("animation show");
        this.$items.eq(this.prevPage - 1).removeClass("show");

        if (html !== undefined) $prevLeft.html(html);

        // set page which is before active page
        this.$items.eq(this.activePage - 1).addClass("show");

        this._async(function() {

          this.options.onend(this.prevPage, this.activePage);
        });

      })
    },
    _doPrev: function() {
      var prev = this.prevPage,
        active = this.activePage,
        $prev = this.$items.eq(prev),
        $active = this.$items.eq(active),
        html,
        // prev page left content
        $activeLeft,
        $beforePrev = this.$items.eq(prev - 1),
        $beforeActive = this.$items.eq(active - 1);

      if (this.end) return this._doEnd("prev", $beforePrev);

      if (prev - 1 !== active) {
        // copy content of left page to prev page left page;
        $activeLeft = $active.find(".left-page");
        html = $activeLeft.html();

        $activeLeft.html($beforePrev.find(".left-page").html());
        $beforePrev.removeClass("show");
        $active.addClass("show");
      }
      if (this.options.speed == 0) {
        $beforeActive.addClass("show");
        $active.addClass("active");
        this._doPrevEnd($active, html, $activeLeft);
        return;
      }
      // add transition css
      $active
        .addClass("animation")
        .one(this.transEndEventName, this._doPrevEnd.bind(this, $active, html, $activeLeft));

      $beforeActive.addClass("show");

      console.timeEnd("prepare animation");
      console.time("paint");
      this._async(function() {
        console.timeEnd("paint");

        $active.addClass("active");
        console.time("transition");
      }, 50);

    },
    _doPrevEnd: function($active, html, $activeLeft) {
      console.timeEnd("transition");
      console.timeEnd("flip page");
      console.time('render new page');
      

      this._async(function() {
        this._reset();
        $active.removeClass("animation");
        if (html !== undefined) $activeLeft.html(html);
        this.$items.eq(this.prevPage)
          .removeClass("active show");

        this._async(function() {
          this.options.onend(this.prevPage, this.activePage);
        });
      });
    },
    /**
     * When the active page is first page or the last page ,
     * the page can't be fliped.
     *
     * @param {string} dir the direction of flip animation.
     * @private
     */
    _doEnd: function(dir) {
      var $el = dir === 'next' ? this.$items.last() : this.$items.first();
      var style = dir === 'next' ? 'rotateY(-15deg)' : 'rotateY(-165deg)';

      $el.css({
        transform: style
      });

      this._async(function() {
        if (!this.options.speed) {
          this._async(function() {
            this._reset();
            this.options.onend(this.prevPage, this.activePage);
            $el.removeAttr("style");
          });
          return;
        }
        // Add animation class and bind transition end function to end element.
        $el.addClass("animation")
          .one(this.transEndEventName, function() {
            $el.removeClass("animation");

            // Reset book flip
            this._reset();

            this._async(function() {
              this.options.onend(this.prevPage, this.activePage);
            });
          }.bind(this));

        // change the transform style to let system do the flip animation.
        this._async(function() {
          $el.removeAttr("style");
        });
      });


    },
    /**
     * initialize animation status
     * @private
     */
    _reset: function() {
      this.end = false;
      this.isAnimating = false;
    },
    /**
     * Async func and bind its `this` points to BookFlip.
     *
     * @param func
     * @param time
     * @private
     */
    _async: function(func, time) {
      time = time || 20;
      setTimeout(func.bind(this), time);
    },

    // public method: flips next
    next: function() {
      this._action('next');
    },
    // public method: flips back
    prev: function() {
      this._action('prev');
    },

    // public method: goes to a specific page
    jump: function(page) {

      // if page isn't  an int number,
      // or page is less than zero or page is bigger than page total number,
      // or page is active page,
      // do nothing.
      if (page != parseInt(page) || page < 0 || page === this.activePage || page >= this.itemsCount) {
        return false;
      }

      page = parseInt(page);

      this._action(page > this.activePage ? 'next' : 'prev', page);

    },
    // public method: check if isAnimating is true
    isActive: function() {
      return this.isAnimating;
    }

  };
  return BookFlip;

});