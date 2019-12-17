pycup.elemental.intrinsic.expy package
======================================

.. automodule:: pycup.elemental.intrinsic.expy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.expy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.expy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.expy.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalEXPY`     Engine class
  :py:class:`.EngineElementalEXPYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalEXPYPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.expy.base
   pycup.elemental.intrinsic.expy.npa
   pycup.elemental.intrinsic.expy.pca
   pycup.elemental.intrinsic.expy.top
