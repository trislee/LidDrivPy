pycup.fft.rfwrd package
=======================

.. automodule:: pycup.fft.rfwrd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================  ==============================
  :py:func:`subroutine() <pycup.fft.rfwrd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.fft.rfwrd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.fft.rfwrd.top.select_engine_class>`  return compatible engine class
  ==========================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==============================  ==============================
  :py:class:`.EngineFFTRFwrd`     Engine class
  :py:class:`.EngineFFTRFwrdNpa`  Engine class for NumPy arrays
  :py:class:`.EngineFFTRFwrdPca`  Engine class for PyCUDA arrays
  ==============================  ==============================

Submodules
----------

.. toctree::

   pycup.fft.rfwrd.base
   pycup.fft.rfwrd.npa
   pycup.fft.rfwrd.pca
   pycup.fft.rfwrd.top
