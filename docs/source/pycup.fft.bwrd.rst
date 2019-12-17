pycup.fft.bwrd package
======================

.. automodule:: pycup.fft.bwrd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================  ==============================
  :py:func:`subroutine() <pycup.fft.bwrd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.fft.bwrd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.fft.bwrd.top.select_engine_class>`  return compatible engine class
  =========================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =============================  ==============================
  :py:class:`.EngineFFTBwrd`     Engine class
  :py:class:`.EngineFFTBwrdNpa`  Engine class for NumPy arrays
  :py:class:`.EngineFFTBwrdPca`  Engine class for PyCUDA arrays
  =============================  ==============================

Submodules
----------

.. toctree::

   pycup.fft.bwrd.base
   pycup.fft.bwrd.npa
   pycup.fft.bwrd.pca
   pycup.fft.bwrd.top
