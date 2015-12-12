/*
  Copyright (C) 2013

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.
*/

almostEqual = function(a, b) {
  if (Math.abs(a - b) < 0.00001) {
    ok(true);
    return;
  }
  ok(false);
}

test('Float32x4 constructor', function() {
  notEqual(undefined, SIMD.Float32x4);  // Type.
  notEqual(undefined, SIMD.Float32x4(1.0, 2.0, 3.0, 4.0));  // New object.
  var f1 = SIMD.Float32x4(1.0, 2.0, 3.0, 4.0);
  var f2 = SIMD.Float32x4.check(f1);
  equal(SIMD.Float32x4.extractLane(f1, 0), SIMD.Float32x4.extractLane(f2, 0), "the value of x should equal");
  equal(SIMD.Float32x4.extractLane(f1, 1), SIMD.Float32x4.extractLane(f2, 1), "the value of y should equal");
  equal(SIMD.Float32x4.extractLane(f1, 2), SIMD.Float32x4.extractLane(f2, 2), "the value of z should equal");
  equal(SIMD.Float32x4.extractLane(f1, 3), SIMD.Float32x4.extractLane(f2, 3), "the value of w should equal");
});

test('Float32x4 scalar getters', function() {
  var a = SIMD.Float32x4(1.0, 2.0, 3.0, 4.0);
  equal(1.0, SIMD.Float32x4.extractLane(a, 0));
  equal(2.0, SIMD.Float32x4.extractLane(a, 1));
  equal(3.0, SIMD.Float32x4.extractLane(a, 2));
  equal(4.0, SIMD.Float32x4.extractLane(a, 3));
});

test('Float32x4 vector getters', function() {
  var a = SIMD.Float32x4(4.0, 3.0, 2.0, 1.0);
  var xxxx = SIMD.Float32x4.swizzle(a, 0, 0, 0, 0);
  var yyyy = SIMD.Float32x4.swizzle(a, 1, 1, 1, 1);
  var zzzz = SIMD.Float32x4.swizzle(a, 2, 2, 2, 2);
  var wwww = SIMD.Float32x4.swizzle(a, 3, 3, 3, 3);
  var wzyx = SIMD.Float32x4.swizzle(a, 3, 2, 1, 0);
  equal(4.0, SIMD.Float32x4.extractLane(xxxx, 0));
  equal(4.0, SIMD.Float32x4.extractLane(xxxx, 1));
  equal(4.0, SIMD.Float32x4.extractLane(xxxx, 2));
  equal(4.0, SIMD.Float32x4.extractLane(xxxx, 3));
  equal(3.0, SIMD.Float32x4.extractLane(yyyy, 0));
  equal(3.0, SIMD.Float32x4.extractLane(yyyy, 1));
  equal(3.0, SIMD.Float32x4.extractLane(yyyy, 2));
  equal(3.0, SIMD.Float32x4.extractLane(yyyy, 3));
  equal(2.0, SIMD.Float32x4.extractLane(zzzz, 0));
  equal(2.0, SIMD.Float32x4.extractLane(zzzz, 1));
  equal(2.0, SIMD.Float32x4.extractLane(zzzz, 2));
  equal(2.0, SIMD.Float32x4.extractLane(zzzz, 3));
  equal(1.0, SIMD.Float32x4.extractLane(wwww, 0));
  equal(1.0, SIMD.Float32x4.extractLane(wwww, 1));
  equal(1.0, SIMD.Float32x4.extractLane(wwww, 2));
  equal(1.0, SIMD.Float32x4.extractLane(wwww, 3));
  equal(1.0, SIMD.Float32x4.extractLane(wzyx, 0));
  equal(2.0, SIMD.Float32x4.extractLane(wzyx, 1));
  equal(3.0, SIMD.Float32x4.extractLane(wzyx, 2));
  equal(4.0, SIMD.Float32x4.extractLane(wzyx, 3));
});

test('Float32x4 abs', function() {
  var a = SIMD.Float32x4(-4.0, -3.0, -2.0, -1.0);
  var c = SIMD.Float32x4.abs(a);
  equal(4.0, SIMD.Float32x4.extractLane(c, 0));
  equal(3.0, SIMD.Float32x4.extractLane(c, 1));
  equal(2.0, SIMD.Float32x4.extractLane(c, 2));
  equal(1.0, SIMD.Float32x4.extractLane(c, 3));
  c = SIMD.Float32x4.abs(SIMD.Float32x4(4.0, 3.0, 2.0, 1.0));
  equal(4.0, SIMD.Float32x4.extractLane(c, 0));
  equal(3.0, SIMD.Float32x4.extractLane(c, 1));
  equal(2.0, SIMD.Float32x4.extractLane(c, 2));
  equal(1.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 neg', function() {
  var a = SIMD.Float32x4(-4.0, -3.0, -2.0, -1.0);
  var c = SIMD.Float32x4.neg(a);
  equal(4.0, SIMD.Float32x4.extractLane(c, 0));
  equal(3.0, SIMD.Float32x4.extractLane(c, 1));
  equal(2.0, SIMD.Float32x4.extractLane(c, 2));
  equal(1.0, SIMD.Float32x4.extractLane(c, 3));
  c = SIMD.Float32x4.neg(SIMD.Float32x4(4.0, 3.0, 2.0, 1.0));
  equal(-4.0, SIMD.Float32x4.extractLane(c, 0));
  equal(-3.0, SIMD.Float32x4.extractLane(c, 1));
  equal(-2.0, SIMD.Float32x4.extractLane(c, 2));
  equal(-1.0, SIMD.Float32x4.extractLane(c, 3));
});


test('Float32x4 add', function() {
  var a = SIMD.Float32x4(4.0, 3.0, 2.0, 1.0);
  var b = SIMD.Float32x4(10.0, 20.0, 30.0, 40.0);
  var c = SIMD.Float32x4.add(a, b);
  equal(14.0, SIMD.Float32x4.extractLane(c, 0));
  equal(23.0, SIMD.Float32x4.extractLane(c, 1));
  equal(32.0, SIMD.Float32x4.extractLane(c, 2));
  equal(41.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 sub', function() {
  var a = SIMD.Float32x4(4.0, 3.0, 2.0, 1.0);
  var b = SIMD.Float32x4(10.0, 20.0, 30.0, 40.0);
  var c = SIMD.Float32x4.sub(a, b);
  equal(-6.0, SIMD.Float32x4.extractLane(c, 0));
  equal(-17.0, SIMD.Float32x4.extractLane(c, 1));
  equal(-28.0, SIMD.Float32x4.extractLane(c, 2));
  equal(-39.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 mul', function() {
  var a = SIMD.Float32x4(4.0, 3.0, 2.0, 1.0);
  var b = SIMD.Float32x4(10.0, 20.0, 30.0, 40.0);
  var c = SIMD.Float32x4.mul(a, b);
  equal(40.0, SIMD.Float32x4.extractLane(c, 0));
  equal(60.0, SIMD.Float32x4.extractLane(c, 1));
  equal(60.0, SIMD.Float32x4.extractLane(c, 2));
  equal(40.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 div', function() {
  var a = SIMD.Float32x4(4.0, 9.0, 8.0, 1.0);
  var b = SIMD.Float32x4(2.0, 3.0, 1.0, 0.5);
  var c = SIMD.Float32x4.div(a, b);
  equal(2.0, SIMD.Float32x4.extractLane(c, 0));
  equal(3.0, SIMD.Float32x4.extractLane(c, 1));
  equal(8.0, SIMD.Float32x4.extractLane(c, 2));
  equal(2.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 min', function() {
  var a = SIMD.Float32x4(-20.0, 10.0, 30.0, 0.5);
  var lower = SIMD.Float32x4(2.0, 1.0, 50.0, 0.0);
  var c = SIMD.Float32x4.min(a, lower);
  equal(-20.0, SIMD.Float32x4.extractLane(c, 0));
  equal(1.0, SIMD.Float32x4.extractLane(c, 1));
  equal(30.0, SIMD.Float32x4.extractLane(c, 2));
  equal(0.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 max', function() {
  var a = SIMD.Float32x4(-20.0, 10.0, 30.0, 0.5);
  var upper = SIMD.Float32x4(2.5, 5.0, 55.0, 1.0);
  var c = SIMD.Float32x4.max(a, upper);
  equal(2.5, SIMD.Float32x4.extractLane(c, 0));
  equal(10.0, SIMD.Float32x4.extractLane(c, 1));
  equal(55.0, SIMD.Float32x4.extractLane(c, 2));
  equal(1.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 reciprocal', function() {
  var a = SIMD.Float32x4(8.0, 4.0, 2.0, -2.0);
  var c = SIMD.Float32x4.reciprocalApproximation(a);
  equal(0.125, SIMD.Float32x4.extractLane(c, 0));
  equal(0.250, SIMD.Float32x4.extractLane(c, 1));
  equal(0.5, SIMD.Float32x4.extractLane(c, 2));
  equal(-0.5, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 reciprocal sqrt', function() {
  var a = SIMD.Float32x4(1.0, 0.25, 0.111111, 0.0625);
  var c = SIMD.Float32x4.reciprocalSqrtApproximation(a);
  almostEqual(1.0, SIMD.Float32x4.extractLane(c, 0));
  almostEqual(2.0, SIMD.Float32x4.extractLane(c, 1));
  almostEqual(3.0, SIMD.Float32x4.extractLane(c, 2));
  almostEqual(4.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 sqrt', function() {
  var a = SIMD.Float32x4(16.0, 9.0, 4.0, 1.0);
  var c = SIMD.Float32x4.sqrt(a);
  equal(4.0, SIMD.Float32x4.extractLane(c, 0));
  equal(3.0, SIMD.Float32x4.extractLane(c, 1));
  equal(2.0, SIMD.Float32x4.extractLane(c, 2));
  equal(1.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 withX', function() {
    var a = SIMD.Float32x4(16.0, 9.0, 4.0, 1.0);
    var c = SIMD.Float32x4.replaceLane(a, 0, 20.0);
    equal(20.0, SIMD.Float32x4.extractLane(c, 0));
    equal(9.0, SIMD.Float32x4.extractLane(c, 1));
    equal(4.0, SIMD.Float32x4.extractLane(c, 2));
    equal(1.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 withY', function() {
    var a = SIMD.Float32x4(16.0, 9.0, 4.0, 1.0);
    var c = SIMD.Float32x4.replaceLane(a, 1, 20.0);
    equal(16.0, SIMD.Float32x4.extractLane(c, 0));
    equal(20.0, SIMD.Float32x4.extractLane(c, 1));
    equal(4.0, SIMD.Float32x4.extractLane(c, 2));
    equal(1.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 withZ', function() {
    var a = SIMD.Float32x4(16.0, 9.0, 4.0, 1.0);
    var c = SIMD.Float32x4.replaceLane(a, 2, 20.0);
    equal(16.0, SIMD.Float32x4.extractLane(c, 0));
    equal(9.0, SIMD.Float32x4.extractLane(c, 1));
    equal(20.0, SIMD.Float32x4.extractLane(c, 2));
    equal(1.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 withW', function() {
    var a = SIMD.Float32x4(16.0, 9.0, 4.0, 1.0);
    var c = SIMD.Float32x4.replaceLane(a, 3, 20.0);
    equal(16.0, SIMD.Float32x4.extractLane(c, 0));
    equal(9.0, SIMD.Float32x4.extractLane(c, 1));
    equal(4.0, SIMD.Float32x4.extractLane(c, 2));
    equal(20.0, SIMD.Float32x4.extractLane(c, 3));
});

test('Float32x4 Int32x4 conversion', function() {
  var m = SIMD.Int32x4(0x3F800000, 0x40000000, 0x40400000, 0x40800000);
  var n = SIMD.Float32x4.fromInt32x4Bits(m);
  equal(1.0, SIMD.Float32x4.extractLane(n, 0));
  equal(2.0, SIMD.Float32x4.extractLane(n, 1));
  equal(3.0, SIMD.Float32x4.extractLane(n, 2));
  equal(4.0, SIMD.Float32x4.extractLane(n, 3));
  n = SIMD.Float32x4(5.0, 6.0, 7.0, 8.0);
  m = SIMD.Int32x4.fromFloat32x4Bits(n);
  equal(0x40A00000, SIMD.Int32x4.extractLane(m, 0));
  equal(0x40C00000, SIMD.Int32x4.extractLane(m, 1));
  equal(0x40E00000, SIMD.Int32x4.extractLane(m, 2));
  equal(0x41000000, SIMD.Int32x4.extractLane(m, 3));
  // Flip sign using bit-wise operators.
  n = SIMD.Float32x4(9.0, 10.0, 11.0, 12.0);
  m = SIMD.Int32x4(0x80000000, 0x80000000, 0x80000000, 0x80000000);
  var nMask = SIMD.Int32x4.fromFloat32x4Bits(n);
  nMask = SIMD.Int32x4.xor(nMask, m); // flip sign.
  n = SIMD.Float32x4.fromInt32x4Bits(nMask);
  equal(-9.0, SIMD.Float32x4.extractLane(n, 0));
  equal(-10.0, SIMD.Float32x4.extractLane(n, 1));
  equal(-11.0, SIMD.Float32x4.extractLane(n, 2));
  equal(-12.0, SIMD.Float32x4.extractLane(n, 3));
  nMask = SIMD.Int32x4.fromFloat32x4Bits(n);
  nMask = SIMD.Int32x4.xor(nMask, m); // flip sign.
  n = SIMD.Float32x4.fromInt32x4Bits(nMask);
  equal(9.0, SIMD.Float32x4.extractLane(n, 0));
  equal(10.0, SIMD.Float32x4.extractLane(n, 1));
  equal(11.0, SIMD.Float32x4.extractLane(n, 2));
  equal(12.0, SIMD.Float32x4.extractLane(n, 3));
  // Should stay unmodified across bit conversions
  m = SIMD.Int32x4(0xFFFFFFFF, 0xFFFF0000, 0x80000000, 0x0);
  var m2 = SIMD.Int32x4.fromFloat32x4Bits(SIMD.Float32x4.fromInt32x4Bits(m));
  equal(SIMD.Int32x4.extractLane(m, 0), SIMD.Int32x4.extractLane(m2, 0));
  equal(SIMD.Int32x4.extractLane(m, 1), SIMD.Int32x4.extractLane(m2, 1));
  equal(SIMD.Int32x4.extractLane(m, 2), SIMD.Int32x4.extractLane(m2, 2));
  equal(SIMD.Int32x4.extractLane(m, 3), SIMD.Int32x4.extractLane(m2, 3));
});

test('Float32x4 comparisons', function() {
  var m = SIMD.Float32x4(1.0, 2.0, 0.1, 0.001);
  var n = SIMD.Float32x4(2.0, 2.0, 0.001, 0.1);
  var cmp;
  cmp = SIMD.Float32x4.lessThan(m, n);
  equal(true, SIMD.Bool32x4.extractLane(cmp, 0));
  equal(false, SIMD.Bool32x4.extractLane(cmp, 1));
  equal(false, SIMD.Bool32x4.extractLane(cmp, 2));
  equal(true, SIMD.Bool32x4.extractLane(cmp, 3));

  cmp = SIMD.Float32x4.lessThanOrEqual(m, n);
  equal(true, SIMD.Bool32x4.extractLane(cmp, 0));
  equal(true, SIMD.Bool32x4.extractLane(cmp, 1));
  equal(false, SIMD.Bool32x4.extractLane(cmp, 2));
  equal(true, SIMD.Bool32x4.extractLane(cmp, 3));

  cmp = SIMD.Float32x4.equal(m, n);
  equal(false, SIMD.Bool32x4.extractLane(cmp, 0));
  equal(true, SIMD.Bool32x4.extractLane(cmp, 1));
  equal(false, SIMD.Bool32x4.extractLane(cmp, 2));
  equal(false, SIMD.Bool32x4.extractLane(cmp, 3));

  cmp = SIMD.Float32x4.notEqual(m, n);
  equal(true, SIMD.Bool32x4.extractLane(cmp, 0));
  equal(false, SIMD.Bool32x4.extractLane(cmp, 1));
  equal(true, SIMD.Bool32x4.extractLane(cmp, 2));
  equal(true, SIMD.Bool32x4.extractLane(cmp, 3));

  cmp = SIMD.Float32x4.greaterThanOrEqual(m, n);
  equal(false, SIMD.Bool32x4.extractLane(cmp, 0));
  equal(true, SIMD.Bool32x4.extractLane(cmp, 1));
  equal(true, SIMD.Bool32x4.extractLane(cmp, 2));
  equal(false, SIMD.Bool32x4.extractLane(cmp, 3));

  cmp = SIMD.Float32x4.greaterThan(m, n);
  equal(false, SIMD.Bool32x4.extractLane(cmp, 0));
  equal(false, SIMD.Bool32x4.extractLane(cmp, 1));
  equal(true, SIMD.Bool32x4.extractLane(cmp, 2));
  equal(false, SIMD.Bool32x4.extractLane(cmp, 3));
});

test('Int32x4 select', function() {
  //var m = SIMD.Int32x4.bool(true, true, false, false);
  var m = SIMD.Bool32x4(true, true, false, false);
  var t = SIMD.Int32x4(1, 2, 3, 4);
  var f = SIMD.Int32x4(5, 6, 7, 8);
  var s = SIMD.Int32x4.select(m, t, f);
  equal(1, SIMD.Int32x4.extractLane(s, 0));
  equal(2, SIMD.Int32x4.extractLane(s, 1));
  equal(7, SIMD.Int32x4.extractLane(s, 2));
  equal(8, SIMD.Int32x4.extractLane(s, 3));
});

test('Int32x4 withX', function() {
    var a = SIMD.Int32x4(1, 2, 3, 4);
    var c = SIMD.Int32x4.replaceLane(a, 0, 20);
    equal(20, SIMD.Int32x4.extractLane(c, 0));
    equal(2, SIMD.Int32x4.extractLane(c, 1));
    equal(3, SIMD.Int32x4.extractLane(c, 2));
    equal(4, SIMD.Int32x4.extractLane(c, 3));
});

test('Int32x4 withY', function() {
    var a = SIMD.Int32x4(1, 2, 3, 4);
    var c = SIMD.Int32x4.replaceLane(a, 1, 20);
    equal(1, SIMD.Int32x4.extractLane(c, 0));
    equal(20, SIMD.Int32x4.extractLane(c, 1));
    equal(3, SIMD.Int32x4.extractLane(c, 2));
    equal(4, SIMD.Int32x4.extractLane(c, 3));
});

test('Int32x4 withZ', function() {
    var a = SIMD.Int32x4(1, 2, 3, 4);
    var c = SIMD.Int32x4.replaceLane(a, 2, 20);
    equal(1, SIMD.Int32x4.extractLane(c, 0));
    equal(2, SIMD.Int32x4.extractLane(c, 1));
    equal(20, SIMD.Int32x4.extractLane(c, 2));
    equal(4, SIMD.Int32x4.extractLane(c, 3));
});

test('Int32x4 withW', function() {
    var a = SIMD.Int32x4(1, 2, 3, 4);
    var c = SIMD.Int32x4.replaceLane(a, 3, 20);
    equal(1, SIMD.Int32x4.extractLane(c, 0));
    equal(2, SIMD.Int32x4.extractLane(c, 1));
    equal(3, SIMD.Int32x4.extractLane(c, 2));
    equal(20, SIMD.Int32x4.extractLane(c, 3));
});

test('Int32x4 and', function() {
  var m = SIMD.Int32x4(0xAAAAAAAA, 0xAAAAAAAA, -1431655766, 0xAAAAAAAA);
  var n = SIMD.Int32x4(0x55555555, 0x55555555, 0x55555555, 0x55555555);
  equal(-1431655766, SIMD.Int32x4.extractLane(m, 0));
  equal(-1431655766, SIMD.Int32x4.extractLane(m, 1));
  equal(-1431655766, SIMD.Int32x4.extractLane(m, 2));
  equal(-1431655766, SIMD.Int32x4.extractLane(m, 3));
  equal(0x55555555, SIMD.Int32x4.extractLane(n, 0));
  equal(0x55555555, SIMD.Int32x4.extractLane(n, 1));
  equal(0x55555555, SIMD.Int32x4.extractLane(n, 2));
  equal(0x55555555, SIMD.Int32x4.extractLane(n, 3));
  var o = SIMD.Int32x4.and(m,n);  // and
  equal(0x0, SIMD.Int32x4.extractLane(o, 0));
  equal(0x0, SIMD.Int32x4.extractLane(o, 1));
  equal(0x0, SIMD.Int32x4.extractLane(o, 2));
  equal(0x0, SIMD.Int32x4.extractLane(o, 3));
});

test('Int32x4 or', function() {
  var m = SIMD.Int32x4(0xAAAAAAAA, 0xAAAAAAAA, 0xAAAAAAAA, 0xAAAAAAAA);
  var n = SIMD.Int32x4(0x55555555, 0x55555555, 0x55555555, 0x55555555);
  var o = SIMD.Int32x4.or(m,n);  // or
  equal(-1, SIMD.Int32x4.extractLane(o, 0));
  equal(-1, SIMD.Int32x4.extractLane(o, 1));
  equal(-1, SIMD.Int32x4.extractLane(o, 2));
  equal(-1, SIMD.Int32x4.extractLane(o, 3));
});

test('Int32x4 xor', function() {
  var m = SIMD.Int32x4(0xAAAAAAAA, 0xAAAAAAAA, 0xAAAAAAAA, 0xAAAAAAAA);
  var n = SIMD.Int32x4(0x55555555, 0x55555555, 0x55555555, 0x55555555);
  n = SIMD.Int32x4.replaceLane(n, 0, 0xAAAAAAAA);
  n = SIMD.Int32x4.replaceLane(n, 1, 0xAAAAAAAA);
  n = SIMD.Int32x4.replaceLane(n, 2, 0xAAAAAAAA);
  n = SIMD.Int32x4.replaceLane(n, 3, 0xAAAAAAAA);
  equal(-1431655766, SIMD.Int32x4.extractLane(n, 0));
  equal(-1431655766, SIMD.Int32x4.extractLane(n, 1));
  equal(-1431655766, SIMD.Int32x4.extractLane(n, 2));
  equal(-1431655766, SIMD.Int32x4.extractLane(n, 3));
  var o = SIMD.Int32x4.xor(m,n);  // xor
  equal(0x0, SIMD.Int32x4.extractLane(o, 0));
  equal(0x0, SIMD.Int32x4.extractLane(o, 1));
  equal(0x0, SIMD.Int32x4.extractLane(o, 2));
  equal(0x0, SIMD.Int32x4.extractLane(o, 3));
});

test('Int32x4 neg', function() {
  var m = SIMD.Int32x4(16, 32, 64, 128);
  var n = SIMD.Int32x4(-1, -2, -3, -4);
  m = SIMD.Int32x4.neg(m);
  n = SIMD.Int32x4.neg(n);
  equal(-16, SIMD.Int32x4.extractLane(m, 0));
  equal(-32, SIMD.Int32x4.extractLane(m, 1));
  equal(-64, SIMD.Int32x4.extractLane(m, 2));
  equal(-128, SIMD.Int32x4.extractLane(m, 3));
  equal(1, SIMD.Int32x4.extractLane(n, 0));
  equal(2, SIMD.Int32x4.extractLane(n, 1));
  equal(3, SIMD.Int32x4.extractLane(n, 2));
  equal(4, SIMD.Int32x4.extractLane(n, 3));
});

test('Int32x4 add', function() {
  var a = SIMD.Int32x4(0xFFFFFFFF, 0xFFFFFFFF, 0x7fffffff, 0x0);
  var b = SIMD.Int32x4(0x1, 0xFFFFFFFF, 0x1, 0xFFFFFFFF);
  var c = SIMD.Int32x4.add(a, b);
  equal(0x0, SIMD.Int32x4.extractLane(c, 0));
  equal(-2, SIMD.Int32x4.extractLane(c, 1));
  equal(-0x80000000, SIMD.Int32x4.extractLane(c, 2));
  equal(-1, SIMD.Int32x4.extractLane(c, 3));
});

test('Int32x4 sub', function() {
  var a = SIMD.Int32x4(0xFFFFFFFF, 0xFFFFFFFF, 0x80000000, 0x0);
  var b = SIMD.Int32x4(0x1, 0xFFFFFFFF, 0x1, 0xFFFFFFFF);
  var c = SIMD.Int32x4.sub(a, b);
  equal(-2, SIMD.Int32x4.extractLane(c, 0));
  equal(0x0, SIMD.Int32x4.extractLane(c, 1));
  equal(0x7FFFFFFF, SIMD.Int32x4.extractLane(c, 2));
  equal(0x1, SIMD.Int32x4.extractLane(c, 3));
});

test('Int32x4 mul', function() {
  var a = SIMD.Int32x4(0xFFFFFFFF, 0xFFFFFFFF, 0x80000000, 0x0);
  var b = SIMD.Int32x4(0x1, 0xFFFFFFFF, 0x80000000, 0xFFFFFFFF);
  var c = SIMD.Int32x4.mul(a, b);
  equal(-1, SIMD.Int32x4.extractLane(c, 0));
  equal(0x1, SIMD.Int32x4.extractLane(c, 1));
  equal(0x0, SIMD.Int32x4.extractLane(c, 2));
  equal(0x0, SIMD.Int32x4.extractLane(c, 3));
});

test('Int32x4 shiftLeftByScalar', function() {
  var a = SIMD.Int32x4(0xffffffff, 0x7fffffff, 0x1, 0x0);
  var b;
  b = SIMD.Int32x4.shiftLeftByScalar(a, 1);
  equal(SIMD.Int32x4.extractLane(b, 0), 0xfffffffe|0);
  equal(SIMD.Int32x4.extractLane(b, 1), 0xfffffffe|0);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x00000002);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
  b = SIMD.Int32x4.shiftLeftByScalar(a, 2);
  equal(SIMD.Int32x4.extractLane(b, 0), 0xfffffffc|0);
  equal(SIMD.Int32x4.extractLane(b, 1), 0xfffffffc|0);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x00000004);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
  b = SIMD.Int32x4.shiftLeftByScalar(a, 30);
  equal(SIMD.Int32x4.extractLane(b, 0), 0xc0000000|0);
  equal(SIMD.Int32x4.extractLane(b, 1), 0xc0000000|0);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x40000000);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
  b = SIMD.Int32x4.shiftLeftByScalar(a, 31);
  equal(SIMD.Int32x4.extractLane(b, 0), 0x80000000|0);
  equal(SIMD.Int32x4.extractLane(b, 1), 0x80000000|0);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x80000000|0);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x0);
});

test('Int32x4 shiftRightLogicalByScalar', function() {
  var a = SIMD.Int32x4(0xffffffff, 0x7fffffff, 0x1, 0x0);
  var b;
  b = SIMD.Int32x4.shiftRightLogicalByScalar(a, 1);
  equal(SIMD.Int32x4.extractLane(b, 0), 0x7fffffff);
  equal(SIMD.Int32x4.extractLane(b, 1), 0x3fffffff);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x00000000);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
  b = SIMD.Int32x4.shiftRightLogicalByScalar(a, 2);
  equal(SIMD.Int32x4.extractLane(b, 0), 0x3fffffff);
  equal(SIMD.Int32x4.extractLane(b, 1), 0x1fffffff);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x00000000);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
  b = SIMD.Int32x4.shiftRightLogicalByScalar(a, 30);
  equal(SIMD.Int32x4.extractLane(b, 0), 0x00000003);
  equal(SIMD.Int32x4.extractLane(b, 1), 0x00000001);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x00000000);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
  b = SIMD.Int32x4.shiftRightLogicalByScalar(a, 31);
  equal(SIMD.Int32x4.extractLane(b, 0), 0x00000001);
  equal(SIMD.Int32x4.extractLane(b, 1), 0x00000000);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x00000000);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
});

test('Int32x4 shiftRightArithmeticByScalar', function() {
  var a = SIMD.Int32x4(0xffffffff, 0x7fffffff, 0x1, 0x0);
  var b;
  b = SIMD.Int32x4.shiftRightArithmeticByScalar(a, 1);
  equal(SIMD.Int32x4.extractLane(b, 0), 0xffffffff|0);
  equal(SIMD.Int32x4.extractLane(b, 1), 0x3fffffff);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x00000000);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
  b = SIMD.Int32x4.shiftRightArithmeticByScalar(a, 2);
  equal(SIMD.Int32x4.extractLane(b, 0), 0xffffffff|0);
  equal(SIMD.Int32x4.extractLane(b, 1), 0x1fffffff);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x00000000);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
  b = SIMD.Int32x4.shiftRightArithmeticByScalar(a, 30);
  equal(SIMD.Int32x4.extractLane(b, 0), 0xffffffff|0);
  equal(SIMD.Int32x4.extractLane(b, 1), 0x00000001);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x00000000);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
  b = SIMD.Int32x4.shiftRightArithmeticByScalar(a, 31);
  equal(SIMD.Int32x4.extractLane(b, 0), 0xffffffff|0);
  equal(SIMD.Int32x4.extractLane(b, 1), 0x00000000);
  equal(SIMD.Int32x4.extractLane(b, 2), 0x00000000);
  equal(SIMD.Int32x4.extractLane(b, 3), 0x00000000);
});

test('Float32x4 shuffle', function() {
  var a = SIMD.Float32x4(1.0, 2.0, 3.0, 4.0);
  var b = SIMD.Float32x4(5.0, 6.0, 7.0, 8.0);
  var xyxy = SIMD.Float32x4.shuffle(a, b, 0, 1, 4, 5);
  var zwzw = SIMD.Float32x4.shuffle(a, b, 2, 3, 6, 7);
  var xxxx = SIMD.Float32x4.shuffle(a, b, 0, 0, 4, 4);
  equal(1.0, SIMD.Float32x4.extractLane(xyxy, 0));
  equal(2.0, SIMD.Float32x4.extractLane(xyxy, 1));
  equal(5.0, SIMD.Float32x4.extractLane(xyxy, 2));
  equal(6.0, SIMD.Float32x4.extractLane(xyxy, 3));
  equal(3.0, SIMD.Float32x4.extractLane(zwzw, 0));
  equal(4.0, SIMD.Float32x4.extractLane(zwzw, 1));
  equal(7.0, SIMD.Float32x4.extractLane(zwzw, 2));
  equal(8.0, SIMD.Float32x4.extractLane(zwzw, 3));
  equal(1.0, SIMD.Float32x4.extractLane(xxxx, 0));
  equal(1.0, SIMD.Float32x4.extractLane(xxxx, 1));
  equal(5.0, SIMD.Float32x4.extractLane(xxxx, 2));
  equal(5.0, SIMD.Float32x4.extractLane(xxxx, 3));
  var c = SIMD.Float32x4.shuffle(a, b, 0, 4, 5, 1);
  var d = SIMD.Float32x4.shuffle(a, b, 2, 6, 3, 7);
  var e = SIMD.Float32x4.shuffle(a, b, 0, 4, 0, 4);
  equal(1.0, SIMD.Float32x4.extractLane(c, 0));
  equal(5.0, SIMD.Float32x4.extractLane(c, 1));
  equal(6.0, SIMD.Float32x4.extractLane(c, 2));
  equal(2.0, SIMD.Float32x4.extractLane(c, 3));
  equal(3.0, SIMD.Float32x4.extractLane(d, 0));
  equal(7.0, SIMD.Float32x4.extractLane(d, 1));
  equal(4.0, SIMD.Float32x4.extractLane(d, 2));
  equal(8.0, SIMD.Float32x4.extractLane(d, 3));
  equal(1.0, SIMD.Float32x4.extractLane(e, 0));
  equal(5.0, SIMD.Float32x4.extractLane(e, 1));
  equal(1.0, SIMD.Float32x4.extractLane(e, 2));
  equal(5.0, SIMD.Float32x4.extractLane(e, 3));
});

test('Int32x4 shuffle', function() {
  var a = SIMD.Int32x4(1, 2, 3, 4);
  var b = SIMD.Int32x4(5, 6, 7, 8);
  var xyxy = SIMD.Int32x4.shuffle(a, b, 0, 1, 4, 5);
  var zwzw = SIMD.Int32x4.shuffle(a, b, 2, 3, 6, 7);
  var xxxx = SIMD.Int32x4.shuffle(a, b, 0, 0, 4, 4);
  equal(1, SIMD.Int32x4.extractLane(xyxy, 0));
  equal(2, SIMD.Int32x4.extractLane(xyxy, 1));
  equal(5, SIMD.Int32x4.extractLane(xyxy, 2));
  equal(6, SIMD.Int32x4.extractLane(xyxy, 3));
  equal(3, SIMD.Int32x4.extractLane(zwzw, 0));
  equal(4, SIMD.Int32x4.extractLane(zwzw, 1));
  equal(7, SIMD.Int32x4.extractLane(zwzw, 2));
  equal(8, SIMD.Int32x4.extractLane(zwzw, 3));
  equal(1, SIMD.Int32x4.extractLane(xxxx, 0));
  equal(1, SIMD.Int32x4.extractLane(xxxx, 1));
  equal(5, SIMD.Int32x4.extractLane(xxxx, 2));
  equal(5, SIMD.Int32x4.extractLane(xxxx, 3));
  var c = SIMD.Int32x4.shuffle(a, b, 0, 4, 5, 1);
  var d = SIMD.Int32x4.shuffle(a, b, 2, 6, 3, 7);
  var e = SIMD.Int32x4.shuffle(a, b, 0, 4, 0, 4);
  equal(1, SIMD.Int32x4.extractLane(c, 0));
  equal(5, SIMD.Int32x4.extractLane(c, 1));
  equal(6, SIMD.Int32x4.extractLane(c, 2));
  equal(2, SIMD.Int32x4.extractLane(c, 3));
  equal(3, SIMD.Int32x4.extractLane(d, 0));
  equal(7, SIMD.Int32x4.extractLane(d, 1));
  equal(4, SIMD.Int32x4.extractLane(d, 2));
  equal(8, SIMD.Int32x4.extractLane(d, 3));
  equal(1, SIMD.Int32x4.extractLane(e, 0));
  equal(5, SIMD.Int32x4.extractLane(e, 1));
  equal(1, SIMD.Int32x4.extractLane(e, 2));
  equal(5, SIMD.Int32x4.extractLane(e, 3));
});

test('Int32x4 vector getters', function() {
  var a = SIMD.Int32x4(4, 3, 2, 1);
  var xxxx = SIMD.Int32x4.swizzle(a, 0, 0, 0, 0);
  var yyyy = SIMD.Int32x4.swizzle(a, 1, 1, 1, 1);
  var zzzz = SIMD.Int32x4.swizzle(a, 2, 2, 2, 2);
  var wwww = SIMD.Int32x4.swizzle(a, 3, 3, 3, 3);
  var wzyx = SIMD.Int32x4.swizzle(a, 3, 2, 1, 0);
  equal(4, SIMD.Int32x4.extractLane(xxxx, 0));
  equal(4, SIMD.Int32x4.extractLane(xxxx, 1));
  equal(4, SIMD.Int32x4.extractLane(xxxx, 2));
  equal(4, SIMD.Int32x4.extractLane(xxxx, 3));
  equal(3, SIMD.Int32x4.extractLane(yyyy, 0));
  equal(3, SIMD.Int32x4.extractLane(yyyy, 1));
  equal(3, SIMD.Int32x4.extractLane(yyyy, 2));
  equal(3, SIMD.Int32x4.extractLane(yyyy, 3));
  equal(2, SIMD.Int32x4.extractLane(zzzz, 0));
  equal(2, SIMD.Int32x4.extractLane(zzzz, 1));
  equal(2, SIMD.Int32x4.extractLane(zzzz, 2));
  equal(2, SIMD.Int32x4.extractLane(zzzz, 3));
  equal(1, SIMD.Int32x4.extractLane(wwww, 0));
  equal(1, SIMD.Int32x4.extractLane(wwww, 1));
  equal(1, SIMD.Int32x4.extractLane(wwww, 2));
  equal(1, SIMD.Int32x4.extractLane(wwww, 3));
  equal(1, SIMD.Int32x4.extractLane(wzyx, 0));
  equal(2, SIMD.Int32x4.extractLane(wzyx, 1));
  equal(3, SIMD.Int32x4.extractLane(wzyx, 2));
  equal(4, SIMD.Int32x4.extractLane(wzyx, 3));
});
