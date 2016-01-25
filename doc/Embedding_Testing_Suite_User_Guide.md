# EmbeddingAPI Test Suite User Guide

## Introduction

This document provides the method to run EmbeddingAPI Test Suite on Android Platform.

## Preconditions

- Setup Ubuntu (12.04 64bit) Host for the Test Environments
- Ensure that you haveset up your host environment for Android compilation .
- Install testkit-lite on Host

## Run EmbeddingAPI test cases

EmbeddingAPI Test Suite is released as a ZIP file. Use this step to install it on the target device:

- Unzip the package on the test machine by running the following command:

$unzip -o webapi-embedding-xwalk-tests-<version\>.zip

- set up an Android device to the host with USB interface.
- Install the package on the test machine by running the following command:

$cd opt

$cd embedding-api-android-tests

$./inst.sh –i

- Uninstall the package on the test machine:

If the console shows 'Failure [INSTALL\_FAILED\_ALREADY\_EXISTS]' when you install it, You need to uninstall it first. You can either uninstall it manually on the android device, or use the following command:

$./inst.sh –u

- Run test cases by running the following command on host:

$cp test.xml $My_Dir

$testkit-lite –f $My\_Dir/tests.xml --comm androidmobile -A -o "$My\_Dir/tests.result.xml"



