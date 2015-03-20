define(function (require, exports, module) {
  var _ = require("underscore");
  var observer = require("pkg!observer");
  var PageHTMLCache = {};
  var SignalCache = {};
  var ErrorMessage = {
    content:"[Connect]: Url can't load",
    signal:"[Connect]: signal file can't be loaded",
    slotObject:"[Connect] Can't find slot object with itemId:"
  };

  observer.on("plugin:end.init", function () {
    observer.trigger("system:register.end", "preload", "connect:end.cache");
  });



  function cache(ebook) {
    var ncx = ebook.get("ncx").points;
    var temp = [];
    var urls = 0;
    var files = 0;

    // find all links of signal files; 
    _.each(ncx, function (item) {
      var obj = {};
      obj.url = item.content;
      urls++;
      if (item.signals) {
        obj.signals = item.signals;
        files++;
      }
      temp.push(obj);
    });

    var check = function () {
      if (urls === _.size(PageHTMLCache) && files === _.size(SignalCache)) {
        observer.trigger("connect:end.cache");
      }
    };

    _.each(temp, function (item) {
      var page;
      ebook.loadByURL(item.url, function (err, xhr) {

        if (err) {
          return  console.error(ErrorMessage.content, item.url, err);
        }

        page = xhr.page;
        // cache pageHTML;
        PageHTMLCache[page] = xhr;
        if (!item.signals) {
          return check();
        }

        ebook.loadByURL(item.signals, function (signalErr, result) {

          if (signalErr) {
            console.error(ErrorMessage.signal, item.signals,signalErr) ;
            return;
          }

          SignalCache[page] = JSON.parse(result.content);
          return check();
        });
      });
    });
  }


  function registerSignal(pageUnit) {
    var page = pageUnit.page,
      units = pageUnit.cache,
      pageEvents = SignalCache[page];

    // check pageEvets isn"t empty
    if (!_.isArray(pageEvents)) {
      return;
    }

    pageEvents.forEach(function (item) {
      var signalItemId = item[0],
        signal = "page:" + item[1],
        slotItemId = item[2],
        slots = item[3],
        slotObject;

      // TODO check the slotObject before bind the singal & slot to pageOb.

      // bind event to pageOb
      pageUnit.pageOb.on(signal, function (itemId) {
        var args = Array.prototype.slice.call(arguments, 1);

        // check the singal sender, if signalItemId is global, 
        // recive all itemId"s message without itself,
        // if signalItemId is a specific id, just recive the specific id's message
        if (signalItemId !== itemId && signalItemId !== "global") {
          return true;
        }

        // didn"t send signal to itself if this signal ItemId bind to "global"
        if (signalItemId === "global" && itemId === slotItemId) {
          return true;
        }

        // Find slotObject tha unit.itemId is slotItemId  
        slotObject = _.find(units, function (unit) {
          return unit.itemId == slotItemId;
        });

        // If it can't find any slotObject, throw error;
        if (!slotObject) {
          return console.error(ErrorMessage.slotObject + slotItemId);
        }

        // If it can't find slot on slotObject,throw error;
        if (!_.isFunction(slotObject[slots])) {
          return console.error("[Connect] Can't find Slot function named '" + slots + "' on ", slotObject,
            "Please make sure the slot is existed and its type is a function");
        }

        // run this slot with signal's message;
        slotObject[slots].apply(slotObject, args);
        return true;
      });
    });
  }

  return {
    registerSignal: registerSignal,
    PageHTMLCache: PageHTMLCache,
    SignalCache: SignalCache,
    cache: cache
  };
});
