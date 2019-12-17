pycup.elemental.derived.mypdfu package
======================================

.. automodule:: pycup.elemental.derived.mypdfu
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.mypdfu.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.mypdfu.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.mypdfu.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineElementalMYPDFU`     Engine class
  :py:class:`.EngineElementalMYPDFUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMYPDFUPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.mypdfu.base
   pycup.elemental.derived.mypdfu.npa
   pycup.elemental.derived.mypdfu.pca
   pycup.elemental.derived.mypdfu.top
