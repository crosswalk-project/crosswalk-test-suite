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

var sp;

test(function() {
  assert_own_property(realsense, "ScenePerception", "realsense should expose ScenePerception");
}, "Check that ScenePerception is present on realsense");

test(function() {
  sp = realsense.ScenePerception;
  assert_true(sp instanceof EventTarget, "ScenePerception inherts EventTarget");
}, "Check that ScenePerception inherts from EventTarget");

test(function() {
  assert_own_property(sp, "init");
  assert_equals(typeof sp.init, "function", "sp.init is function type");
}, "Check that init() exists");

test(function() {
  assert_own_property(sp, "start");
  assert_equals(typeof sp.start, "function", "sp.start is function type");
}, "Check that start() exists");

test(function() {
  assert_own_property(sp, "stop");
  assert_equals(typeof sp.stop, "function", "sp.stop is function type");
}, "Check that stop() exists");

test(function() {
  assert_own_property(sp, "reset");
  assert_equals(typeof sp.reset, "function", "sp.reset is function type");
}, "Check that reset() exists");

test(function() {
  assert_own_property(sp, "destroy");
  assert_equals(typeof sp.destroy, "function", "sp.destroy is function type");
}, "Check that destroy() exists");

test(function() {
  assert_own_property(sp, "enableReconstruction");
  assert_equals(typeof sp.enableReconstruction, "function", "sp.enableReconstruction is function type");
}, "Check that enableReconstruction() exists");

test(function() {
  assert_own_property(sp, "enableRelocalization");
  assert_equals(typeof sp.enableRelocalization, "function", "sp.enableRelocalization is function type");
}, "Check that enableRelocalization() exists");

test(function() {
  assert_own_property(sp, "isReconstructionEnabled");
  assert_equals(typeof sp.isReconstructionEnabled, "function", "sp.isReconstructionEnabled is function type");
}, "Check that isReconstructionEnabled() exists");

test(function() {
  assert_own_property(sp, "getSample");
  assert_equals(typeof sp.getSample, "function", "sp.getSample is function type");
}, "Check that getSample() exists");

test(function() {
  assert_own_property(sp, "getVertices");
  assert_equals(typeof sp.getVertices, "function", "sp.getVertices is function type");
}, "Check that getVertices() exists");

test(function() {
  assert_own_property(sp, "getVolumePreview");
  assert_equals(typeof sp.getVolumePreview, "function", "sp.getVolumePreview is function type");
}, "Check that getVolumePreview() exists");

test(function() {
  assert_own_property(sp, "getNormals");
  assert_equals(typeof sp.getNormals, "function", "sp.getNormals is function type");
}, "Check that getNormals() exists");

test(function() {
  assert_own_property(sp, "queryVolumePreview");
  assert_equals(typeof sp.queryVolumePreview, "function", "sp.queryVolumePreview is function type");
}, "Check that queryVolumePreview() exists");

test(function() {
  assert_own_property(sp, "getVoxelResolution");
  assert_equals(typeof sp.getVoxelResolution, "function", "sp.getVoxelResolution is function type");
}, "Check that getVoxelResolution() exists");

test(function() {
  assert_own_property(sp, "getVoxelSize");
  assert_equals(typeof sp.getVoxelSize, "function", "sp.getVoxelSize is function type");
}, "Check that getVoxelSize() exists");

test(function() {
  assert_own_property(sp, "getInternalCameraIntrinsics");
  assert_equals(typeof sp.getInternalCameraIntrinsics, "function", "sp.getInternalCameraIntrinsics is function type");
}, "Check that getInternalCameraIntrinsics() exists");

test(function() {
  assert_own_property(sp, "getMeshingThresholds");
  assert_equals(typeof sp.getMeshingThresholds, "function", "sp.getMeshingThresholds is function type");
}, "Check that getMeshingThresholds() exists");

test(function() {
  assert_own_property(sp, "getMeshingResolution");
  assert_equals(typeof sp.getMeshingResolution, "function", "sp.getMeshingResolution is function type");
}, "Check that getMeshingResolution() exists");

test(function() {
  assert_own_property(sp, "getMeshData");
  assert_equals(typeof sp.getMeshData, "function", "sp.getMeshData is function type");
}, "Check that getMeshData() exists");

test(function() {
  assert_own_property(sp, "getSurfaceVoxels");
  assert_equals(typeof sp.getSurfaceVoxels, "function", "sp.getSurfaceVoxels is function type");
}, "Check that getSurfaceVoxels() exists");

test(function() {
  assert_own_property(sp, "saveMesh");
  assert_equals(typeof sp.saveMesh, "function", "sp.saveMesh is function type");
}, "Check that saveMesh() exists");

test(function() {
  assert_own_property(sp, "setMeshingResolution");
  assert_equals(typeof sp.setMeshingResolution, "function", "sp.setMeshingResolution is function type");
}, "Check that setMeshingResolution() exists");

test(function() {
  assert_own_property(sp, "setMeshingThresholds");
  assert_equals(typeof sp.setMeshingThresholds, "function", "sp.setMeshingThresholds is function type");
}, "Check that setMeshingThresholds() exists");

test(function() {
  assert_own_property(sp, "setCameraPose");
  assert_equals(typeof sp.setCameraPose, "function", "sp.setCameraPose is function type");
}, "Check that setCameraPose() exists");

test(function() {
  assert_own_property(sp, "setMeshingUpdateConfigs");
  assert_equals(typeof sp.setMeshingUpdateConfigs, "function", "sp.setMeshingUpdateConfigs is function type");
}, "Check that setMeshingUpdateConfigs() exists");

test(function() {
  assert_own_property(sp, "configureSurfaceVoxelsData");
  assert_equals(typeof sp.configureSurfaceVoxelsData, "function", "sp.configureSurfaceVoxelsData is function type");
}, "Check that configureSurfaceVoxelsData() exists");

test(function() {
  assert_own_property(sp, "setMeshingRegion");
  assert_equals(typeof sp.setMeshingRegion, "function", "sp.setMeshingRegion is function type");
}, "Check that setMeshingRegion() exists");

test(function() {
  assert_own_property(sp, "clearMeshingRegion");
  assert_equals(typeof sp.clearMeshingRegion, "function", "sp.clearMeshingRegion is function type");
}, "Check that clearMeshingRegion() exists");

test(function() {
  assert_own_property(sp, "onchecking");
}, "Check that onchecking exists");

test(function() {
  assert_own_property(sp, "onerror");
}, "Check that onerror exists");

test(function() {
  assert_own_property(sp, "onmeshupdated");
}, "Check that onmeshupdated exists");

test(function() {
  assert_own_property(sp, "onsampleprocessed");
}, "Check that onsampleprocessed exists");

async_test(function(t) {
  sp.init()
    .then(function() {
      t.done();
    })
    .catch(function(ex) {
      assert_unreached("unreached here, get error: " + ex.name);
    });
}, "Check that initialize a Scene Perception without config");

async_test(function(t) {
  sp.start()
    .then(function() {
      t.done();
    })
    .catch(function(ex) {
      assert_unreached("unreached here, get error: " + ex.name);
    });
}, "Check that start a scene perception");

promise_test(function() {
  return sp.isReconstructionEnabled()
    .then(function(enable) {
      assert_equals(typeof enable, "boolean");
    })
    .catch(function(ex) {
      assert_unreached("unreached here, get error: " + ex.name);
    });
}, "Check that whether integration of upcoming camera stream into 3D volume is enabled");

promise_test(function() {
  return sp.enableReconstruction()
    .then(function() {
      assert_unreached("unreached here when miss enable parameter");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");	
    });
}, "Check that enableReconstruction should throw a SPError when miss enable parameter");

promise_test(function() {
  return sp.enableReconstruction(null)
    .then(function() {
      assert_unreached("unreached here when enable is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that enableReconstruction should reject with a SPError when enable is null");

promise_test(function() {
  return sp.enableRelocalization()
    .then(function() {
      assert_unreached("unreached here when miss enable parameter");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that enableRelocalization should reject with a SPError when miss enable parameter");

promise_test(function() {
  return sp.enableRelocalization(null)
    .then(function() {
      assert_unreached("unreached here when enable is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that enableRelocalization should reject with a SPError when enable is null");

promise_test(function() {
  return sp.getSurfaceVoxels(null)
    .then(function() {
      assert_unreached("unreached here when region is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that getSurfaceVoxels should reject with a SPError when region is null");

promise_test(function() {
  return sp.queryVolumePreview(null)
    .then(function() {
      assert_unreached("unreached here when cameraPose is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that queryVolumePreview should reject with a SPError when cameraPose is null");

promise_test(function() {
  return sp.saveMesh(null)
    .then(function() {
      assert_unreached("unreached here when info is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that saveMesh should reject with a SPError when info is null");

promise_test(function() {
  return sp.setCameraPose()
    .then(function() {
      assert_unreached("unreached here when miss cameraPose parameter");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that setCameraPose should reject with a SPError when miss cameraPose parameter");

promise_test(function() {
  return sp.setCameraPose(null)
    .then(function() {
      assert_unreached("unreached here when cameraPose is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");	
    });
}, "Check that setCameraPose should throw a Error exception when cameraPose is null");

promise_test(function() {
  return sp.setMeshingRegion()
    .then(function() {
      assert_unreached("unreached here when miss region parameter");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that setMeshingRegion should reject with a SPError when miss region parameter");

promise_test(function() {
  return sp.setMeshingRegion(null)
    .then(function() {
      assert_unreached("unreached here when region is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that setMeshingRegion should reject with a SPError when region is null");

promise_test(function() {
  return sp.setMeshingResolution()
    .then(function() {
      assert_unreached("unreached here when miss resolution parameter");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");	
    });
}, "Check that setMeshingResolution should reject with a SPError when miss resolution parameter");

promise_test(function() {
  return sp.setMeshingResolution(null)
    .then(function() {
      assert_unreached("unreached here when resolution is null");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that setMeshingResolution should reject with a SPError when resolution is null");

promise_test(function() {
  return sp.configureSurfaceVoxelsData()
    .then(function() {
      assert_unreached("unreached here when miss config parameter");
    })
    .catch(function(ex) {
      assert_equals(ex.error, "param_unsupported");
    });
}, "Check that configureSurfaceVoxelsData should reject with a SPError when miss config parameter");

promise_test(function() {
  return sp.configureSurfaceVoxelsData(null)
    .then(function() {
    assert_unreached("unreached here when config is null");
  })
  .catch(function(ex) {
    assert_equals(ex.error, "param_unsupported");
  });
}, "Check that configureSurfaceVoxelsData should reject with a SPError when config is null");

promise_test(function() {
  return sp.stop()
    .then(function() {
      assert_true(true, "stop successfully");
    })
    .catch(function(ex) {
      assert_unreached("unreached here, get error: " + ex.name);
    });
}, "Check that stop scene perception");

promise_test(function() {
  return sp.destroy()
    .then(function() {
      assert_true(true, "destroy successfully");
    })
    .catch(function(ex) {
      assert_unreached("unreached here, get error: " + ex.name);
    });
}, "Check that destroy scene perception");
