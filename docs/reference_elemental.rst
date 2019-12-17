
.. _sec-ref-elemental:

Elemental
=========

Elemental operations act on the individual elements of all independent arrays in an array of arrays.
For example, :py:mod:`.sqrtx` computes the square root of all elements of all independent arrays contained in the array of arrays :math:`\mathsf{x}`.

These operations can be either in-place (the output of the operation is stored in the input array of arrays), or out-of-place (the output of the operation is stored in an array of arrays that is not the input).
In PyCUP, out-of-place operations are distinguished by having a *y* in their name, with the convention being that the output of an operation on the array of arrays :math:`\mathsf{y}` is stored in :math:`\mathsf{x}`.
For example, the out-of-place square root operation :py:mod:`.sqrty` stores the element-wise square root of array of arrays :math:`\mathsf{y}` in the array of arrays :math:`\mathsf{x}`.
The corresponding in-place operation :py:mod:`.sqrtx` stores the element-wise square root of array of arrays :math:`\mathsf{x}` in the array of arrays :math:`\mathsf{x}`.

Elemental operations can be divided into two categories: :ref:`sec-ref-elemental-intrinsic` and :ref:`sec-ref-elemental-derived`.
Intrinsic operations call language-specific existing implementations of standard functions, while for derived operations, no such language-specific implementation exists.
For example, both NumPy and C++ have standard implementations of the absolute value function, so instead of implementing the absolute value function from scratch, the intrinsic operation :py:mod:`.absx` simply calls one of these existing implementations.
By contrast, neither NumPy nor C++ have standard implementations of a function that scales an array of arrays by an array and adds a second array, so the derived operation :py:mod:`.axpb` implements this from scratch.

PyCUP elemental operations have a naming convention based on their constituent unary and binary operations:

  * {} -
    multiplication; e.g. `xy` : :math:`\mathsf{x} \leftarrow \mathsf{x} \mathsf{y}`

  * `p` -
    plus/addition; e.g. `xpy` : :math:`\mathsf{x} \leftarrow \mathsf{x} + \mathsf{y}`

  * `s` -
    minus/subtraction; e.g. xsy : :math:`\mathsf{x} \leftarrow \mathsf{x} - \mathsf{y}`

  * `m` -
    magnitude/absolute value; e.g. `mx` : :math:`\mathsf{x} \leftarrow | \mathsf{x} |`

  * `j` -
    complex conjugate; e.g. `jx` : :math:`\mathsf{x} \leftarrow \mathsf{x}^*`

  * `r` -
    multiplicative reciprocal; e.g. `rx` : :math:`\mathsf{x} \leftarrow 1 / \mathsf{x}`

  * `w` -
    power; e.g. `xwa` : :math:`\mathsf{x} \leftarrow \mathsf{x}^a`

  * `h` -
    natural exponential; e.g. `xhy` : :math:`\mathsf{x} \leftarrow \mathsf{x} e^\mathsf{y}`

  * `f` -
    flush left; e.g. `xpafry` reads `(xpa)ry` : :math:`\mathsf{x} \leftarrow ( \mathsf{x} + a) / \mathsf{y}`

  * `l` -
    flush right; e.g. `xrlypa` reads `xr(ypa)` : :math:`\mathsf{x} \leftarrow \mathsf{x} / ( \mathsf{y} + a)`

  * `i` -
    datatype kind upcasting : converts unsigned integer to integer and converts float to complex.

.. currentmodule:: pycup.elemental.derived

.. _sec-ref-elemental-derived:

Derived
-------

.. autosummary::

  ax
  axpb
  axpby
  axpy
  axy
  aypb
  aypz
  dx
  dy
  iy
  jxy
  m2lysz
  m2y
  m2ypa
  m2yz
  mxpa
  mxpafry
  mypd
  mypdfu
  myu
  pplysz
  ppxpa
  ppyparlppzpb
  rx
  ry
  xhay
  xhu
  xhy
  xiu
  xiy
  xjy
  xjyiu
  xjyu
  xpa
  xpafu
  xpafwb
  xpam2y
  xpau
  xpay
  xpayz
  xpd
  xpdfu
  xpdy
  xpiay
  xpy
  xpyfrz
  xry
  xsa
  xsy
  xu
  xy
  xypa
  xywd
  y
  yiz
  yju
  yjz
  ypa
  ypau
  ypz
  ysz
  yz

.. currentmodule:: pycup.elemental.intrinsic

.. _sec-ref-elemental-intrinsic:

Intrinsic
---------

.. autosummary::

  absx
  absy
  bcopy
  bfill
  conjx
  conjy
  copy
  dcasty
  expx
  expy
  fill
  maxxa
  maxxd
  maxxy
  minxa
  minxd
  minxy
  powxa
  powxd
  powya
  powyd
  sqrtx
  sqrty
  sqrx
  sqry
  ucasty
