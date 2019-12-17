pycup.elemental.intrinsic.minxy package
=======================================

.. automodule:: pycup.elemental.intrinsic.minxy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.minxy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.minxy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.minxy.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalMINXY`     Engine class
  :py:class:`.EngineElementalMINXYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMINXYPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.minxy.base
   pycup.elemental.intrinsic.minxy.npa
   pycup.elemental.intrinsic.minxy.pca
   pycup.elemental.intrinsic.minxy.top
