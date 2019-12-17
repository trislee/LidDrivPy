pycup.elemental.intrinsic.conjy package
=======================================

.. automodule:: pycup.elemental.intrinsic.conjy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.conjy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.conjy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.conjy.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalCONJY`     Engine class
  :py:class:`.EngineElementalCONJYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalCONJYPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.conjy.base
   pycup.elemental.intrinsic.conjy.npa
   pycup.elemental.intrinsic.conjy.pca
   pycup.elemental.intrinsic.conjy.top
