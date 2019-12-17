pycup.elemental.derived.pplxsa package
======================================

.. automodule:: pycup.elemental.derived.pplxsa
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.pplxsa.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.pplxsa.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.pplxsa.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineElementalPPLXSA`     Engine class
  :py:class:`.EngineElementalPPLXSANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalPPLXSAPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.pplxsa.base
   pycup.elemental.derived.pplxsa.npa
   pycup.elemental.derived.pplxsa.pca
   pycup.elemental.derived.pplxsa.top
