pycup.elemental.derived.xpy package
===================================

.. automodule:: pycup.elemental.derived.xpy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpy.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXPY`     Engine class
  :py:class:`.EngineElementalXPYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPYPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpy.base
   pycup.elemental.derived.xpy.npa
   pycup.elemental.derived.xpy.pca
   pycup.elemental.derived.xpy.top
