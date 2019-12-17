.. _sec-ref-reduction:

Reduction
=========

Reduction operations reduce each independent array in an array of arrays to a single scalar.
These operations include sums (:py:mod:`.sum`), maximum values (:py:mod:`.max`), and dot products (:py:mod:`.dot`).
An additional *a* in the subpackage name indicates that the absolute value of the independent array is taken before the reduction operation is performed.

.. currentmodule:: pycup.reduction

.. autosummary::

  amax
  amin
  argamax
  argamin
  argmax
  argmin
  bdot
  bidot
  bzcc
  dot
  max
  min
  nl1
  nl2
  nlp
  rfftsum
  sos
  sum