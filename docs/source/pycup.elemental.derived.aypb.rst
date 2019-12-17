pycup.elemental.derived.aypb package
====================================

.. automodule:: pycup.elemental.derived.aypb
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.aypb.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.aypb.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.aypb.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalAYPB`     Engine class
  :py:class:`.EngineElementalAYPBNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalAYPBPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.aypb.base
   pycup.elemental.derived.aypb.npa
   pycup.elemental.derived.aypb.pca
   pycup.elemental.derived.aypb.top
