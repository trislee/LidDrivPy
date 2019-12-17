pycup.elemental.intrinsic.copy package
======================================

.. automodule:: pycup.elemental.intrinsic.copy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.copy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.copy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.copy.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalCOPY`     Engine class
  :py:class:`.EngineElementalCOPYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalCOPYPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.copy.base
   pycup.elemental.intrinsic.copy.npa
   pycup.elemental.intrinsic.copy.pca
   pycup.elemental.intrinsic.copy.top
