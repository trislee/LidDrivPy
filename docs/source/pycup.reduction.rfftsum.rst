pycup.reduction.rfftsum package
===============================

.. automodule:: pycup.reduction.rfftsum
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==================================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.rfftsum.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.rfftsum.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.rfftsum.top.select_engine_class>`  return compatible engine class
  ==================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ======================================  ==============================
  :py:class:`.EngineReductionRFFTSum`     Engine class
  :py:class:`.EngineReductionRFFTSumNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionRFFTSumPca`  Engine class for PyCUDA arrays
  ======================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.rfftsum.base
   pycup.reduction.rfftsum.npa
   pycup.reduction.rfftsum.pca
   pycup.reduction.rfftsum.top
