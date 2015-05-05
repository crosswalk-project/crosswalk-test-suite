# Chromium Feature Verification Guide

## 1. Introduction

Crosswalk is based on Chromium, when a new version of Chromium is released, it will be rebased to the new version, and integrate the new features of new Chromium, what we need to do is check whether these new features work well after rebase.

This document provides how to verify the Chromium features on Crosswalk, including: List Chromium feature samples, run the samples on Chromium beta and Crosswalk Project for Android, Feedback result.

## 2. List Chromium feature samples

- Chromium feature samples

    <a href="http://zqzhang.github.io/demo/chromestatus/">http://zqzhang.github.io/demo/chromestatus/</a>

    These samples are leveraged from <a href="https://www.chromestatus.com">https://www.chromestatus.com</a>.

- How to create the samples
  
    eg: for Chromium 43 features
        
    -  Leverage the samples url in
       <a href="https://www.chromestatus.com/features#=43">https://www.chromestatus.com/features#=43</a>

    - Create <a href="http://zqzhang.github.io/demo/chromestatus/m43.html">http://zqzhang.github.io/demo/chromestatus/m43.html</a> to list the samples url.
     
## 3. Run on Crosswalk Project for Android

- Download Crosswalk on Android

    <a href="https://download.01.org/crosswalk/releases/crosswalk/android/canary/">https://download.01.org/crosswalk/releases/crosswalk/android/canary/</a>
    
- Install Crosswalk on Android

    $ adb install XWalkRuntimeLib.apk

- Install XWalkCoreShell

    $ adb install XWalkCoreShell.apk

- Run feature samples on XWalkCoreShell

  - Start XWalkCoreShell

  - Open the samples url

        eg: http://zqzhang.github.io/demo/chromestatus/m43.html

  - Test the samples by each links.

## 4. Run on Chromium beta for Android

- Download and Install Chromium beta for Android

    Note: Chrome beta need to match the version of Crosswalk version.

- Run feature samples on Chromium beta for Android

  - Start Chromium beta

  - Open the samples url

        eg: http://zqzhang.github.io/demo/chromestatus/m43.html

  - Test the samples by each links.

## 5. Feedback

- Report Chromium&lt;version num&gt;-Feature_tests.xlsx

    eg: Chromium43-Feature_tests.xlsx

- Create Pull Request to add features

    Only need to integrate those samples which have corresponding Crosswalk JIRA feature requests. Because these samples shall be executed in Crosswalk regular testing.
  
    - sampleapp android tests path

        /crosswalk-test-suite/misc/sampleapp-android-tests/sampleapp


More help link: <a href="https://lists.crosswalk-project.org/mailman/listinfo/crosswalk-dev">Crosswalk-dev mailing list</a>
