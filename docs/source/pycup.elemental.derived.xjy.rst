pycup.elemental.derived.xjy package
===================================

.. automodule:: pycup.elemental.derived.xjy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xjy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xjy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xjy.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXJY`     Engine class
  :py:class:`.EngineElementalXJYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXJYPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xjy.base
   pycup.elemental.derived.xjy.npa
   pycup.elemental.derived.xjy.pca
   pycup.elemental.derived.xjy.top
