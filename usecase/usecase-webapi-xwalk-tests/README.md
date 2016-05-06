# Usecase WebAPI examples

## Introduction
This test suite contains some web samples that demonstrate use of W3C standard APIs, Crosswalk extension Web API features.

## Preconditions for building the test suite:
* Get the demo-express repo.

  ```Bash
  $ git clone https://github.com/crosswalk-project/demo-express.git
  ```

* Copy all the files in demo-express/samples to the samples directory of current directory.

  ```Bash
  $ cd usecase/usecase-webapi-xwalk-tests
  $ cp -dpRv </path/to/demo-express/samples>/* ./samples/
  ```

* Get the latest fingerprint.zip from [crosswalk-android-extensions](https://github.com/crosswalk-project/crosswalk-android-extensions/releases), unzip it and copy the unzipped files to ```samples/FingerPrint/fingerprint``` directory.

  ```Bash
  $ unzip fingerprint.zip -d </path/to/samples/FingerPrint/fingerprint>
  ```

## Authors:

* Lin, Wanming <wanming.lin@intel.com>


## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
