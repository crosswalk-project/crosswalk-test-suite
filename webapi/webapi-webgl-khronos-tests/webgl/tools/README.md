## Introduction

We have a update tool for sync Khronos conformance-1.0.3. 
- You can run it manually by starting the `import-conformance-tests.py` executable 
from the root of your local crosswalk-test-suite working directory like this:

```
./webapi/webapi-webgl-khronos-tests/webgl/tools/import-conformance-tests.py
```


## Usage of update tool

1. If download to a new folder:</br>
<code>
./tools/import-conformance-tests.py version destination 
</code>
2. If copy from an existing clone of the khronos WebGL repository:</br>
<code>
./tools/import-conformance-tests.py version destination -e pathToRepo
</code>

