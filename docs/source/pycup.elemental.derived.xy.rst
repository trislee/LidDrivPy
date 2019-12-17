pycup.elemental.derived.xy package
==================================

.. automodule:: pycup.elemental.derived.xy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =====================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xy.top.select_engine_class>`  return compatible engine class
  =====================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =================================  ==============================
  :py:class:`.EngineElementalXY`     Engine class
  :py:class:`.EngineElementalXYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXYPca`  Engine class for PyCUDA arrays
  =================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xy.base
   pycup.elemental.derived.xy.npa
   pycup.elemental.derived.xy.pca
   pycup.elemental.derived.xy.top
