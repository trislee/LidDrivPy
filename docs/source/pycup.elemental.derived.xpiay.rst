pycup.elemental.derived.xpiay package
=====================================

.. automodule:: pycup.elemental.derived.xpiay
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpiay.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpiay.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpiay.top.select_engine_class>`  return compatible engine class
  ========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalXPIAY`     Engine class
  :py:class:`.EngineElementalXPIAYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPIAYPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpiay.base
   pycup.elemental.derived.xpiay.npa
   pycup.elemental.derived.xpiay.pca
   pycup.elemental.derived.xpiay.top
