[![Build Status](https://travis-ci.org/rokuz/pygeom.svg?branch=master)](https://travis-ci.org/rokuz/pygeom)
[![Coverage Status](https://coveralls.io/repos/github/rokuz/pygeom/badge.svg?branch=master)](https://coveralls.io/github/rokuz/pygeom?branch=master)

# pygeom
2d/3d math library.

The following classes are available:
- **Vec2**. It represents 2D vector.
    Features:
    - Swizzling like in shader languages (GLSL, HLSL, etc.);
    - Mathematical operations;
    - Comparison operations;
    - Special vector operations: length, normalization, dot and cross products.
- **Line2**. It represents 2D line.
    Features:
    - Projection of 2D point to line;
    - The shortest distance between 2D point and line.
- **Tri2**. It represents 2D triangle.
    Features:
    - Checking for degeneration;
    - Checking for point inside.
- **Vec3**. It represents 3D vector.
    Features:
    - Swizzling like in shader languages (GLSL, HLSL, etc.);
    - Mathematical operations;
    - Comparison operations;
    - Special vector operations: length, normalization, dot and cross products.
    
The following functions are available:
- Linear interpolation;
- Clamp and saturate in shader languages (GLSL, HLSL, etc.).

##Authors and License
MIT License

Copyright (c) 2017 Roman Kuznetsov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
