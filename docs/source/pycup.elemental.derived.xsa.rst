pycup.elemental.derived.xsa package
===================================

.. automodule:: pycup.elemental.derived.xsa
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xsa.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xsa.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xsa.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXSA`     Engine class
  :py:class:`.EngineElementalXSANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXSAPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xsa.base
   pycup.elemental.derived.xsa.npa
   pycup.elemental.derived.xsa.pca
   pycup.elemental.derived.xsa.top
