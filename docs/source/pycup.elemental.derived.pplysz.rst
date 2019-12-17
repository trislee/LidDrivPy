pycup.elemental.derived.pplysz package
======================================

.. automodule:: pycup.elemental.derived.pplysz
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.pplysz.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.pplysz.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.pplysz.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineElementalPPLYSZ`     Engine class
  :py:class:`.EngineElementalPPLYSZNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalPPLYSZPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.pplysz.base
   pycup.elemental.derived.pplysz.npa
   pycup.elemental.derived.pplysz.pca
   pycup.elemental.derived.pplysz.top
