/*
 * Copyright (c) 2013, Intel Corporation.
 *
 * This program is licensed under the terms and conditions of the
 * Apache License, version 2.0.  The full text of the Apache License is at
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 */
var Sound = function (config) {
  config = config || {};
  config.url = config.url || '';
  config.loop = (config.loop === true ? true : false);

  var self = this;
  smokesignals.convert(this);

  this.ready = false;
  this.isPlaying = false;

  this.audio = new Audio();

  this.audio.addEventListener('canplaythrough', function () {
    var firstTime = !self.ready;

    self.ready = true;

    if (firstTime) {
      self.emit('ready');
    }
  });

  this.audio.addEventListener('pause', function () {
    self.isPlaying = false;
  });

  this.audio.addEventListener('play', function () {
    self.isPlaying = true;
  });

  // this is to work around Android xwalk not looping audio
  // when the loop attribute is set:
  // https://github.com/crosswalk-project/crosswalk/issues/659
  this.audio.addEventListener('ended', function () {
    self.isPlaying = false;
    if (config.loop) {
      self.play();
    }
  });

  this.audio.autoplay = false;
  this.audio.preload = 'auto';
  this.audio.src = config.url;
};

Sound.prototype.play = function () {
  if (!this.ready) {
    return;
  }

  if (!this.isPlaying) {
    this.audio.play();
  }
};

Sound.prototype.pause = function () {
  this.audio.pause();
};
