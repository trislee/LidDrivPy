pycup.elemental.derived.xsy package
===================================

.. automodule:: pycup.elemental.derived.xsy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xsy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xsy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xsy.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXSY`     Engine class
  :py:class:`.EngineElementalXSYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXSYPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xsy.base
   pycup.elemental.derived.xsy.npa
   pycup.elemental.derived.xsy.pca
   pycup.elemental.derived.xsy.top
