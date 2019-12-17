pycup.elemental.intrinsic.conjx package
=======================================

.. automodule:: pycup.elemental.intrinsic.conjx
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.conjx.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.conjx.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.conjx.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalCONJX`     Engine class
  :py:class:`.EngineElementalCONJXNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalCONJXPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.conjx.base
   pycup.elemental.intrinsic.conjx.npa
   pycup.elemental.intrinsic.conjx.pca
   pycup.elemental.intrinsic.conjx.top
