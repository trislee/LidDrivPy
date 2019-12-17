pycup.elemental.derived.jxy package
===================================

.. automodule:: pycup.elemental.derived.jxy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.jxy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.jxy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.jxy.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalJXY`     Engine class
  :py:class:`.EngineElementalJXYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalJXYPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.jxy.base
   pycup.elemental.derived.jxy.npa
   pycup.elemental.derived.jxy.pca
   pycup.elemental.derived.jxy.top
