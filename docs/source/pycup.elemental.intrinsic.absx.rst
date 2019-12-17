pycup.elemental.intrinsic.absx package
======================================

.. automodule:: pycup.elemental.intrinsic.absx
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.absx.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.absx.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.absx.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalABSX`     Engine class
  :py:class:`.EngineElementalABSXNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalABSXPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.absx.base
   pycup.elemental.intrinsic.absx.npa
   pycup.elemental.intrinsic.absx.pca
   pycup.elemental.intrinsic.absx.top
