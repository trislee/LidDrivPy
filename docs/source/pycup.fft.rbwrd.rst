pycup.fft.rbwrd package
=======================

.. automodule:: pycup.fft.rbwrd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================  ==============================
  :py:func:`subroutine() <pycup.fft.rbwrd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.fft.rbwrd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.fft.rbwrd.top.select_engine_class>`  return compatible engine class
  ==========================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==============================  ==============================
  :py:class:`.EngineFFTRBwrd`     Engine class
  :py:class:`.EngineFFTRBwrdNpa`  Engine class for NumPy arrays
  :py:class:`.EngineFFTRBwrdPca`  Engine class for PyCUDA arrays
  ==============================  ==============================

Submodules
----------

.. toctree::

   pycup.fft.rbwrd.base
   pycup.fft.rbwrd.npa
   pycup.fft.rbwrd.pca
   pycup.fft.rbwrd.top
