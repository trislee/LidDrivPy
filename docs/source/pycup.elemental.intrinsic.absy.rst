pycup.elemental.intrinsic.absy package
======================================

.. automodule:: pycup.elemental.intrinsic.absy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.absy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.absy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.absy.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalABSY`     Engine class
  :py:class:`.EngineElementalABSYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalABSYPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.absy.base
   pycup.elemental.intrinsic.absy.npa
   pycup.elemental.intrinsic.absy.pca
   pycup.elemental.intrinsic.absy.top
