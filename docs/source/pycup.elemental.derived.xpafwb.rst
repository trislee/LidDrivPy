pycup.elemental.derived.xpafwb package
======================================

.. automodule:: pycup.elemental.derived.xpafwb
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpafwb.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpafwb.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpafwb.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineElementalXPAFWB`     Engine class
  :py:class:`.EngineElementalXPAFWBNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPAFWBPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpafwb.base
   pycup.elemental.derived.xpafwb.npa
   pycup.elemental.derived.xpafwb.pca
   pycup.elemental.derived.xpafwb.top
