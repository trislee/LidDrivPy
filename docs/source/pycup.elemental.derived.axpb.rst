pycup.elemental.derived.axpb package
====================================

.. automodule:: pycup.elemental.derived.axpb
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.axpb.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.axpb.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.axpb.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalAXPB`     Engine class
  :py:class:`.EngineElementalAXPBNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalAXPBPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.axpb.base
   pycup.elemental.derived.axpb.npa
   pycup.elemental.derived.axpb.pca
   pycup.elemental.derived.axpb.top
