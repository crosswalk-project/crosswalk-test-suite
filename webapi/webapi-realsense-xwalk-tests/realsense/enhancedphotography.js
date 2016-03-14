/*
Copyright (c) 2016 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors
  may be used to endorse or promote products derived from this work without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

var depthMask;
var depthRefocus;
var measurement;
var motionEffect;
var paster;
var photoCapture;
var photoUtils;
var segmentation;
var xdmUtils;

test(function() {
  assert_own_property(realsense, "DepthEnabledPhotography",
    "realsense should expose DepthEnabledPhotography");
  assert_equals(typeof realsense.DepthEnabledPhotography, "object");
}, "Check that DepthEnabledPhotography is present on realsense");

test(function() {
  depthMask = new realsense.DepthEnabledPhotography.DepthMask();
  assert_equals(typeof depthMask, "object");
}, "Check that construct a DepthMask object");

var tests = [
  ["init", typeof depthMask.init, "function"],
  ["computeFromCoordinate", typeof depthMask.computeFromCoordinate, "function"],
  ["computeFromThreshold", typeof depthMask.computeFromThreshold, "function"]
];

tests.forEach(function(item) {
  test(function() {
   assert_own_property(depthMask, item[0]);
   assert_equals(item[1], item[2]);
  }, "Check that DepthMask has implement " + item[0] + " method");
});

test(function() {
  depthRefocus = new realsense.DepthEnabledPhotography.DepthRefocus();
  assert_equals(typeof depthRefocus, "object");
}, "Check that construct a DepthRefocus object");

tests = [
  ["init", typeof depthRefocus.init, "function"],
  ["apply", typeof depthRefocus.apply, "function"]
];

tests.forEach(function(item) {
  test(function() {
   assert_own_property(depthRefocus, item[0]);
   assert_equals(item[1], item[2]);
  }, "Check that DepthRefocus has implement " + item[0] + " method");
});

test(function() {
  measurement = new realsense.DepthEnabledPhotography.Measurement();
  assert_equals(typeof measurement, "object");
}, "Check that construct a Measurement object");

tests = [
  ["measureDistance", typeof measurement.measureDistance, "function"],
  ["measureUADistance", typeof measurement.measureUADistance, "function"],
  ["queryUADataSize", typeof measurement.queryUADataSize, "function"],
  ["queryUAData", typeof measurement.queryUAData, "function"]
];

tests.forEach(function(item) {
  test(function() {
   assert_own_property(measurement, item[0]);
   assert_equals(item[1], item[2]);
  }, "Check that Measurement has implement " + item[0] + " method");
});

test(function() {
  motionEffect = new realsense.DepthEnabledPhotography.MotionEffect();
  assert_equals(typeof motionEffect, "object");
}, "Check that construct a MotionEffect object");

tests = [
  ["init", typeof motionEffect.init, "function"],
  ["apply", typeof motionEffect.apply, "function"]
];

tests.forEach(function(item) {
  test(function() {
   assert_own_property(motionEffect, item[0]);
   assert_equals(item[1], item[2]);
  }, "Check that MotionEffect has implement " + item[0] + " method");
});

test(function() {
  paster = new realsense.DepthEnabledPhotography.Paster();
  assert_equals(typeof paster, "object");
}, "Check that construct a Paster object");

tests = [
  ["getPlanesMap", typeof paster.getPlanesMap, "function"],
  ["setPhoto", typeof paster.setPhoto, "function"],
  ["setSticker", typeof paster.setSticker, "function"],
  ["paste", typeof paster.paste, "function"],
  ["previewSticker", typeof paster.previewSticker, "function"]
];

tests.forEach(function(item) {
  test(function() {
   assert_own_property(paster, item[0]);
   assert_equals(item[1], item[2]);
  }, "Check that Paster has implement " + item[0] + " method");
});

navigator.getUserMedia({ video: true }, function getUserMediaSuccess(stream) {
  test(function() {
    photoCapture = new realsense.DepthEnabledPhotography.PhotoCapture(stream);
  }, "Check that construct photoCapture with MediaStream");

  test(function() {
    assert_true(photoCapture instanceof EventTarget, "photoCapture instance of EventTarget");
  }, "Check that photoCapture instance of EventTarget");

  tests = [
    ["getDepthImage", typeof photoCapture.getDepthImage, "function"],
    ["takePhoto", typeof photoCapture.takePhoto, "function"],
    ["previewStream", typeof photoCapture.previewStream, "object"]
  ];

  tests.forEach(function(item) {
    test(function() {
     assert_own_property(photoCapture, item[0]);
     assert_equals(item[1], item[2]);
    }, "Check that PhotoCapture has implement " + item[0] + " method");
  });

  test(function() {
    assert_own_property(photoCapture, "onerror");
  }, "Check that PhotoCapture has implement onerror");

  test(function() {
    assert_own_property(photoCapture, "ondepthquality");
  }, "Check that PhotoCapture has implement ondepthquality");

  test(function () {
    assert_readonly(photoCapture, "previewStream", "previewStream is readonly");
  }, "Check that previewStream is readonly");

  promise_test(function() {
    photoCapture.getDepthImage()
      .then(function(image) {
        assert_true(image instanceof Image);
        // Image interface
        assert_own_property(image, "format", "image has format property");
        assert_own_property(image, "data", "image has data property");
        assert_own_property(image, "height", "image has height property");
        assert_own_property(image, "width", "image has width property");
        assert_readonly(image, "format", "format is readonly");
        assert_readonly(image, "data", "data is readonly");
        assert_readonly(image, "height", "height is readonly");
        assert_readonly(image, "width", "width is readonly");
        assert_equals(typeof image.format, "object", "format is type of object");
        assert_equals(typeof image.data, "ArrayBuffer", "data is type of ArrayBuffer");
        assert_equals(typeof image.height, "number", "height is type of number");
        assert_equals(typeof image.width, "number", "width is type of number");
      })
      .catch(function(ex) {
        assert_unreached("get unexpected error: " + ex.error);
      });
  }, "Check that getDepthImage() returns a promise with the latest available depth image");

  promise_test(function() {
    photoCapture.takePhoto()
      .then(function(photo) {
        assert_true(photo instanceof Photo);
      })
      .catch(function(ex) {
        assert_unreached("get unexpected error: " + ex.error);
      });
  }, "Check that takePhoto() returns a promise with the photo instance");

}, function(ex) {
  assert_unreached("Access to audio and video stream get error: " + ex.message);
});

test(function() {
  assert_own_property(realsense.DepthEnabledPhotography, "PhotoUtils");
  photoUtils = realsense.DepthEnabledPhotography.PhotoUtils;
  assert_equals(typeof photoUtils, "object");
}, "Check that is PhotoUtils is present on realsense.DepthEnabledPhotography");

tests = [
  ["colorResize", typeof photoUtils.colorResize, "function"],
  ["commonFOV", typeof photoUtils.commonFOV, "function"],
  ["depthResize", typeof photoUtils.depthResize, "function"],
  ["enhanceDepth", typeof photoUtils.enhanceDepth, "function"],
  ["getDepthQuality", typeof photoUtils.getDepthQuality, "function"],
  ["photoCrop", typeof photoUtils.photoCrop, "function"],
  ["photoRotate", typeof photoUtils.photoRotate, "function"]
];

tests.forEach(function(item) {
  test(function() {
   assert_own_property(photoUtils, item[0]);
   assert_equals(item[1], item[2]);
  }, "Check that Paster has implement " + item[0] + " method");
});

test(function() {
  segmentation = new realsense.DepthEnabledPhotography.Segmentation();
  assert_equals(typeof segmentation, "object");
}, "Check that construct a Segmentation object");

tests = [
  ["objectSegment", typeof segmentation.objectSegment, "function"],
  ["redo", typeof segmentation.redo, "function"],
  ["refineMask", typeof segmentation.refineMask, "function"],
  ["undo", typeof segmentation.undo, "function"],
];

tests.forEach(function(item) {
  test(function() {
   assert_own_property(segmentation, item[0]);
   assert_equals(item[1], item[2]);
  }, "Check that Segmentation has implement " + item[0] + " method");
});

test(function() {
  assert_own_property(realsense.DepthEnabledPhotography, "XDMUtils");
  xdmUtils = realsense.DepthEnabledPhotography.XDMUtils;
  assert_equals(typeof xdmUtils, "object");
}, "Check that XDMUtils is present on realsense.DepthEnabledPhotography");

tests = [
  ["isXDM", typeof xdmUtils.isXDM, "function"],
  ["loadXDM", typeof xdmUtils.loadXDM, "function"],
  ["saveXDM", typeof xdmUtils.saveXDM, "function"]
];

tests.forEach(function(item) {
  test(function() {
   assert_own_property(xdmUtils, item[0]);
   assert_equals(item[1], item[2]);
  }, "Check that XDMUtils has implement " + item[0] + " method");
});

tests = [
  [function() { depthMask.init(); },
    "DepthMask.init throw TypeError when missing argument"],
  [function() { depthMask.init(null); },
    "DepthMask.init throw TypeError when photo parameter is null"],
  [function() { depthRefocus.init(); },
    "DepthRefocus.init throw TypeError when missing argument"],
  [function() { depthRefocus.init(null); },
    "DepthRefocus.init throw TypeError when focusPoint parameter is null"],
  [function() { motionEffect.init(); },
    "MotionEffect.init throw TypeError when missing argument"],
  [function() { motionEffect.init(null); },
    "MotionEffect.init throw TypeError when focusPoint parameter is null"],
  [function() { xdmUtils.saveXDM(); },
    "XDMUtils.saveXDM throw TypeError when missing argument"],
  [function() { xdmUtils.saveXDM(null); },
    "XDMUtils.saveXDM throw TypeError when blob parameter is null"]
];

tests.forEach(function(item) {
  test(function() {
    assert_throws(new TypeError(), item[0]);
  }, "Check that " + item[1]);
});

promise_test(function() {
  return xdmUtils.isXDM()
    .then(function() {
      assert_unreached("unreached here when miss blob argument");
    })
    .catch(function(ex) {
      assert_equals(ex.name, "TypeError")
    });
}, "Check that XDMUtils.isXDM throw TypeError when missing argument");

promise_test(function() {
  return xdmUtils.isXDM(null)
    .then(function() {
      assert_unreached("unreached here when blob is null");
  })
  .catch(function(ex) {
      assert_equals(ex.name, "TypeError")
  });
}, "Check that XDMUtils.isXDM throw TypeError blob is null");

promise_test(function() {
  return xdmUtils.loadXDM()
    .then(function() {
      assert_unreached("unreached here when miss blob argument");
    })
    .catch(function(ex) {
      assert_equals(ex.name, "TypeError")
    });
}, "Check that XDMUtils.loadXDM throw TypeError when missing argument");

promise_test(function() {
  return xdmUtils.loadXDM(null)
    .then(function() {
      assert_unreached("unreached here when blob is null");
    })
    .catch(function(ex) {
      assert_equals(ex.name, "TypeError")
    });
}, "Check that XDMUtils.loadXDM throw TypeError when blob is null");

promise_test(function() {
  return depthMask.computeFromCoordinate()
    .then(function() {
      assert_unreached("unreached here when miss coordinate argument");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported")
    });
}, "Check that DepthMask.computeFromCoordinate throw DEPError when missing argument");

promise_test(function() {
  return depthMask.computeFromCoordinate(null)
    .then(function() {
      assert_unreached("unreached here when coordinate is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported")
    });
}, "Check that DepthMask.computeFromCoordinate throw DEPError when coordinate is null");

promise_test(function() {
  return depthMask.computeFromThreshold()
    .then(function() {
      assert_unreached("unreached here when miss depthThreshold argument");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported")
    });
}, "Check that DepthMask.computeFromThreshold throw DEPError when missing argument");

promise_test(function() {
  return depthMask.computeFromThreshold(null)
    .then(function() {
      assert_unreached("unreached here when depthThreshold is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported")
    });
}, "Check that DepthMask.computeFromThreshold throw DEPError when depthThreshold is null");

promise_test(function() {
  return depthRefocus.apply()
    .then(function() {
      assert_unreached("unreached here when miss focusPoint argument");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported")
    });
}, "Check that depthRefocus.apply throw DEPError when missing argument");

promise_test(function() {
  return depthRefocus.apply(null)
    .then(function() {
      assert_unreached("unreached here when focusPoint is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported")
    });
}, "Check that depthRefocus.apply throw DEPError when focusPoint is null");

promise_test(function(t) {
  var blob = new Blob(["TEST"]);
  return xdmUtils.isXDM(blob)
    .then(function(result) {
      assert_false(result);
    });
}, "Check that isXDM return false if the blob data isn't XDM format");
