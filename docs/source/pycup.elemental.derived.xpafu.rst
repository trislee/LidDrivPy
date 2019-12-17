pycup.elemental.derived.xpafu package
=====================================

.. automodule:: pycup.elemental.derived.xpafu
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpafu.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpafu.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpafu.top.select_engine_class>`  return compatible engine class
  ========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalXPAFU`     Engine class
  :py:class:`.EngineElementalXPAFUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPAFUPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpafu.base
   pycup.elemental.derived.xpafu.npa
   pycup.elemental.derived.xpafu.pca
   pycup.elemental.derived.xpafu.top
