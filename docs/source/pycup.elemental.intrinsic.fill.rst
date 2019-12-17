pycup.elemental.intrinsic.fill package
======================================

.. automodule:: pycup.elemental.intrinsic.fill
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.fill.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.fill.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.fill.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalFILL`     Engine class
  :py:class:`.EngineElementalFILLNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalFILLPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.fill.base
   pycup.elemental.intrinsic.fill.npa
   pycup.elemental.intrinsic.fill.pca
   pycup.elemental.intrinsic.fill.top
