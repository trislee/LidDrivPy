pycup.elemental.derived.ry package
==================================

.. automodule:: pycup.elemental.derived.ry
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =====================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.ry.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.ry.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.ry.top.select_engine_class>`  return compatible engine class
  =====================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =================================  ==============================
  :py:class:`.EngineElementalRY`     Engine class
  :py:class:`.EngineElementalRYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalRYPca`  Engine class for PyCUDA arrays
  =================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.ry.base
   pycup.elemental.derived.ry.npa
   pycup.elemental.derived.ry.pca
   pycup.elemental.derived.ry.top
