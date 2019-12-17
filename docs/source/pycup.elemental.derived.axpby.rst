pycup.elemental.derived.axpby package
=====================================

.. automodule:: pycup.elemental.derived.axpby
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.axpby.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.axpby.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.axpby.top.select_engine_class>`  return compatible engine class
  ========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalAXPBY`     Engine class
  :py:class:`.EngineElementalAXPBYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalAXPBYPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.axpby.base
   pycup.elemental.derived.axpby.npa
   pycup.elemental.derived.axpby.pca
   pycup.elemental.derived.axpby.top
