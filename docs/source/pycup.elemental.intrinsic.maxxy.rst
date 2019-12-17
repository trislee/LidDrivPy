pycup.elemental.intrinsic.maxxy package
=======================================

.. automodule:: pycup.elemental.intrinsic.maxxy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.maxxy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.maxxy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.maxxy.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalMAXXY`     Engine class
  :py:class:`.EngineElementalMAXXYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMAXXYPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.maxxy.base
   pycup.elemental.intrinsic.maxxy.npa
   pycup.elemental.intrinsic.maxxy.pca
   pycup.elemental.intrinsic.maxxy.top
