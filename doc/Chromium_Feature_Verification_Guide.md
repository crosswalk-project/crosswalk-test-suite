# Chromium Feature Verification Guide

## Introduction

In each milestone (generally 6 weeks), Crosswalk Project is trying to re-base
to latest upstream Chromium Beta, which also involve some new features enabled
by default by the Chromium Beta.

This guide provides a mean to verify the new features brought into Crosswalk
Project by the code re-base, by comparing the samples that Chromium features
used running on Crosswalk Project and Chrome Beta with same Chromium version.

## How to do the feature verification?

### List samples referenced by Chromium features

Google Chrome has an [implementation status](https://www.chromestatus.com/)
which lists all new features with samples attached to each milestone.

Searching the milestone, for example `=45`, in the implementation status page,
one can get all features listed for the milestone. Or one can directly
navigate to https://www.chromestatus.com/features#=45 for the features of M45.

Then create an .html file, say `m45.html`, to list all the features and
corresponding samples' online links, classified the feature list by the
features' implementation status:

- **Features enabled by default**: if a feature is enabled by default on
  Chromium, it shall be supported by Crosswalk Project. And this kind of
  features and samples are what we should care about.
- **Features behind a flag**: if a feature is behind a flag, it shall not be
  supported by Crosswalk Project. Thus leave this kind of feature to next
  version(s) of Crosswalk Project rebases to upstream Chromium, when they are
  enabled by default.
- **Features deprecated**: if a feature is deprecated from Chromium, it shall
  not be supported by Crosswalk Project either. Thus no need to check such kind
  of features.

After that, push the .html file to a GitHub repository `gh-pages` brach, one
can access to the page as GitHub pages, for example,
https://zqzhang.github.io/demo/chromestatus/m45.html

### Run the samples on Chrome Beta for Android

- First please download and install Chrome Beta for Android on the device under
  test (DUT). Note that the Chrome Beta browser should have the same version of
  Chromium as Crosswalk Project.
- Open the Chrome Beta browser and navigate to the online sample page, say
  https://zqzhang.github.io/demo/chromestatus/m45.html
- Check the samples one-by-one and record the output as reference.

### Run the samples on Crosswalk Project for Android

- Build and install a web application for the samples in the GitHub page for
  Crosswalk Project for Android, e.g. following the instructions at
  [here](https://github.com/zqzhang/demo#demos-on-android).
- Open the web application, check the samples one-by-one and record the output.
- Compare the output with that of Chrome Beta browser. If they are the same,
  corresponding feature is verified; otherwise report an issue.

### Run the samples on Crosswalk Project for Linux (optinal)

- Build and install a web application for the samples in the GitHub page for
  Crosswalk Project for Linux, e.g. following the instructions at
  [here](https://github.com/zqzhang/demo#demos-on-linux).
- Open the web application, check the samples one-by-one and record the output.
- Compare the output with that of Chrome Beta browser. If they are the same,
  corresponding feature is verified; otherwise report an issue.

### Report the testing results

- Yes, one can record all results in a spreadsheet with the following info:
  - Chromium version and link to Chrome implementation status.
  - Feature list.
  - Feature description.
  - Feature specification.
  - Implementation status.
  - Upstream samples.
  - Result of Chrome Beta for Android.
  - Result of Crosswalk Project for Android.
  - Result of Crosswalk Project for Linux (optional).
- Report the results and analysis to JIRA bug if there is a feature request
  such as [XWALK-4800](https://crosswalk-project.org/jira/browse/XWALK-4800).
- Report the results and analysis to
  [crosswalk-dev](https://lists.crosswalk-project.org/mailman/listinfo/crosswalk-dev)
  mailing list.
  [Here](https://lists.crosswalk-project.org/pipermail/crosswalk-dev/2015-September/003101.html)
  is an example.