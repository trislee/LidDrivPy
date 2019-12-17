pycup.fft.fwrd package
======================

.. automodule:: pycup.fft.fwrd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================  ==============================
  :py:func:`subroutine() <pycup.fft.fwrd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.fft.fwrd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.fft.fwrd.top.select_engine_class>`  return compatible engine class
  =========================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =============================  ==============================
  :py:class:`.EngineFFTFwrd`     Engine class
  :py:class:`.EngineFFTFwrdNpa`  Engine class for NumPy arrays
  :py:class:`.EngineFFTFwrdPca`  Engine class for PyCUDA arrays
  =============================  ==============================

Submodules
----------

.. toctree::

   pycup.fft.fwrd.base
   pycup.fft.fwrd.npa
   pycup.fft.fwrd.pca
   pycup.fft.fwrd.top
