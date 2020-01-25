Underactuated Robotics
======================

*Algorithms for Walking, Running, Swimming, Flying, and Manipulation*

<http://underactuated.mit.edu/>

![CI](https://github.com/RussTedrake/underactuated/workflows/CI/badge.svg)

Follow the installation instructions in 
http://underactuated.mit.edu/underactuated.html?ch=drake


To view the text locally
------------------------

Make sure to initialize the submodules:

```
git submodule update --init --recursive
```

The textbook should then be viewable by opening `underactuated.html` in your
browser.

You'll need to run a local webserver for the code includes (via ajax) to work. I
used the instructions at 
https://websitebeaver.com/set-up-localhost-on-macos-high-sierra-apache-mysql-and-php-7-with-sslhttps
and just pointed by root doc directory directly at my underactuated checkout.


To run the unit tests using CMake
---------------------------------
CircleCI currently runs the tests using CMake; this will soon be removed in favor of the Bazel workflow below.

```
$ mkdir build && cd build
$ cmake -Ddrake_DIR=PATH_TO_DRAKE/lib/cmake/drake ..
$ make
$ ctest .
```

To run the unit tests using Bazel
---------------------------------
GitHub actions runs the tests using Bazel.  This is preferred, and will replace the CMake workflow once it has complete coverage.  See [#245](https://github.com/RussTedrake/underactuated/issues/245).
```
bazel test //...
```

To run linters
--------------

```
$ pycodestyle
$ pydocstyle
```

To run the auto-linter
----------------------

macOS:
```
$ yapf -i -r -p .
```

Ubuntu Bionic:
```
$ yapf3 -i -r -p .
```


To get experimental drake binaries
-----------------------------------

As described at http://github.com/RobotLocomotion/drake/issues/7926, use

On your drake PR, use
```
@drake-jenkins-bot linux-bionic-unprovisioned-gcc-bazel-experimental-snopt-packaging please
@drake-jenkins-bot mac-mojave-unprovisioned-clang-bazel-experimental-snopt-packaging please
```
Then examine the last lines of the console output from those builds for the 
binary urls.  
