
.. _sec-ref-fft:

FFT
===

FFT operations execute discrete Fourier transforms on independent arrays using a fast Fourier transform algorithm from the NVIDIA cuFFT library if a GPU is enabled, or from NumPy if no GPU is enabled.
FFT operations can be divided into two categories: forward transforms (indicated by an *f* in the subpackage name) and backward transforms (indicated by a *b* in the subpackage name).
FFT operations can also be divided into either real-to-complex (indicated by an *r* in the subpackage name) or complex-to-complex, depending on the datatype of the input array of arrays.

.. currentmodule:: pycup.fft

.. autosummary::

  bwrd
  fwrd
  rbwrd
  rfwrd