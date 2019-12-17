pycup.elemental.derived.m2lysz package
======================================

.. automodule:: pycup.elemental.derived.m2lysz
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.m2lysz.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.m2lysz.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.m2lysz.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineElementalM2LYSZ`     Engine class
  :py:class:`.EngineElementalM2LYSZNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalM2LYSZPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.m2lysz.base
   pycup.elemental.derived.m2lysz.npa
   pycup.elemental.derived.m2lysz.pca
   pycup.elemental.derived.m2lysz.top
