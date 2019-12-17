pycup.elemental.derived.m2ypa package
=====================================

.. automodule:: pycup.elemental.derived.m2ypa
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.m2ypa.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.m2ypa.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.m2ypa.top.select_engine_class>`  return compatible engine class
  ========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalM2YPA`     Engine class
  :py:class:`.EngineElementalM2YPANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalM2YPAPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.m2ypa.base
   pycup.elemental.derived.m2ypa.npa
   pycup.elemental.derived.m2ypa.pca
   pycup.elemental.derived.m2ypa.top
