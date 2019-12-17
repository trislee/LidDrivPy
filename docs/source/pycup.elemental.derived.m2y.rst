pycup.elemental.derived.m2y package
===================================

.. automodule:: pycup.elemental.derived.m2y
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.m2y.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.m2y.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.m2y.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalM2Y`     Engine class
  :py:class:`.EngineElementalM2YNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalM2YPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.m2y.base
   pycup.elemental.derived.m2y.npa
   pycup.elemental.derived.m2y.pca
   pycup.elemental.derived.m2y.top
