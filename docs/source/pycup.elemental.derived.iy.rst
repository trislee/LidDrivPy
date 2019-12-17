pycup.elemental.derived.iy package
==================================

.. automodule:: pycup.elemental.derived.iy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =====================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.iy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.iy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.iy.top.select_engine_class>`  return compatible engine class
  =====================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =================================  ==============================
  :py:class:`.EngineElementalIY`     Engine class
  :py:class:`.EngineElementalIYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalIYPca`  Engine class for PyCUDA arrays
  =================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.iy.base
   pycup.elemental.derived.iy.npa
   pycup.elemental.derived.iy.pca
   pycup.elemental.derived.iy.top
