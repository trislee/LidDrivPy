pycup.elemental.derived.xpdfu package
=====================================

.. automodule:: pycup.elemental.derived.xpdfu
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpdfu.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpdfu.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpdfu.top.select_engine_class>`  return compatible engine class
  ========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalXPDFU`     Engine class
  :py:class:`.EngineElementalXPDFUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPDFUPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpdfu.base
   pycup.elemental.derived.xpdfu.npa
   pycup.elemental.derived.xpdfu.pca
   pycup.elemental.derived.xpdfu.top
