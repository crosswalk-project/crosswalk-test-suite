function runGenericSensorTests(sensorType, readingType, verifyReading, arrReading) {
  async_test(t => {
    let sensor = new sensorType();
    sensor.start();
    sensor.onchange = t.step_func_done(() => {
      assert_true(verifyReading(sensor.reading));
      assert_equals(sensor.state, "activated");
      sensor.stop();
    });
    sensor.onerror = t.step_func_done(event => {
      assert_unreached(event.error.name + ":" + event.error.message);
    });
  }, "event change fired");

  async_test(t => {
    let sensor = new sensorType();
    sensor.start();
    sensor.onactivate = t.step_func_done(() => {
      let cachedReading = sensor.reading;
      let cached1 = arrReading(cachedReading);
      sensor.stop();
      let cached2 = arrReading(cachedReading);
      for (var i = 0; i < cached2.length; i++) {
        assert_equals(cached1[i], cached2[i]);
      }
    });
    sensor.onerror = t.step_func_done(event => {
      assert_unreached(event.error.name + ":" + event.error.message);
    });
  }, "Test that sensor reading must be immutable.");

  async_test(t => {
    let sensor1 = new sensorType();
    let sensor2 = new sensorType();
    sensor1.start();
    sensor2.start();
    sensor1.onactivate = t.step_func_done(() => {
      cachedReading1 = sensor1.reading;
      cachedReading2 = sensor2.reading;
      //both sensors share the same reading instance
      assert_equals(cachedReading1, cachedReading2);
      //after first sensor stops its reading is null, second sensor remains
      sensor1.stop();
      assert_equals(sensor1.reading, null);
      assert_true(sensor2.reading instanceof readingType);
      sensor2.stop();
    });
    sensor1.onerror = t.step_func_done(event => {
      assert_unreached(event.error.name + ":" + event.error.message);
    });
  }, "Test that sensor reading is correct.");

  async_test(t => {
    let sensor = new sensorType();
    sensor.start();
    let cachedReading1;
    sensor.onactivate = function() {
      cachedReading1 = sensor.reading;
    };
    sensor.onerror = t.step_func_done(event => {
      assert_unreached(event.error.name + ":" + event.error.message);
    });
    t.step_timeout(() => {
      sensor.onchange = t.step_func_done(() => {
        let cachedReading2 = sensor.reading;
        assert_not_equals(cachedReading1, cachedReading2);
        sensor.stop();
      });
    }, 1000);
  }, "Test that the sensor reading is updated when time passes.");

  test(() => {
    let sensor, start_return;
    sensor = new sensorType();
    //The default sensor.reading is 'null'
    assert_equals(sensor.reading, null);
    //The default sensor.state is 'idle'
    assert_equals(sensor.state, "idle");
    start_return = sensor.start();
    //The sensor.state changes to 'activating' after sensor.start()
    assert_equals(sensor.state, "activating");
    //TODO: The permission is not ready.
    //the sensor.start() return undefined
    assert_equals(start_return, undefined);
    //throw an InvalidStateError exception when state is neither idle nor errored
    assert_throws("InvalidStateError", () => { sensor.start(); }, "start() twice");
    sensor.stop();
  }, "Test that sensor.start() is correct.");

  test(() => {
    let sensor, stop_return;
    sensor = new sensorType();
    sensor.start();
    stop_return = sensor.stop();
    //The sensor.state changes to 'idle' after sensor.stop()
    assert_equals(sensor.state, "idle");
    //the sensor.reading is null after executing stop() method
    assert_equals(sensor.reading, null);
    //throw an InvalidStateError exception when state is either idle or errored
    assert_throws("InvalidStateError", () => { sensor.stop(); }, "stop() twice");
    //the sensor.stop() returns undefined
    assert_equals(stop_return, undefined);
  }, "Test that sensor.stop() is correct.");
}

function runGenericSensorBrowsingContext(sensorType) {
  async_test(t => {
    window.onmessage = t.step_func(e => {
      assert_equals(e.data, "SecurityError");
      t.done();
    });
  }, "throw a 'SecurityError' when firing sensor readings within iframes");

  async_test(t => {
    let sensor = new sensorType();
    sensor.start();
    sensor.onactivate = t.step_func_done(() => {
      assert_not_equals(sensor.reading, null);
      let cachedReading = sensor.reading;
      let win = window.open('', '_blank');
      assert_equals(sensor.reading, cachedReading);
      win.close();
      sensor.stop();
    });
    sensor.onerror = t.step_func_done(event => {
      assert_unreached(event.error.name + ":" + event.error.message);
    });
  }, "sensor readings can not be fired on the background tab");
}

function runGenericSensorInsecureContext(sensorType, sensorName) {
  test(() => {
    assert_throws('SecurityError', () => {
      let sensor = new sensorType();
    });
  }, "throw a 'SecurityError' when construct " + sensorName + " in an insecure context");
}

function runGenericSensorOnerror(sensorType, sensorName) {
  async_test(t => {
    let sensor = new sensorType();
    sensor.onactivate = t.step_func_done(assert_unreached);
    sensor.onerror = t.step_func_done(event => {
      assert_equals(sensor.state, 'errored');
      assert_equals(event.error.name, 'NotFoundError');
    });
    sensor.start();
  }, "Test that 'onerror' event is fired when " + sensorName + " sensor is not supported");
}
