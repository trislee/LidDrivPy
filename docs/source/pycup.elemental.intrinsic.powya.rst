pycup.elemental.intrinsic.powya package
=======================================

.. automodule:: pycup.elemental.intrinsic.powya
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.powya.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.powya.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.powya.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalPOWYA`     Engine class
  :py:class:`.EngineElementalPOWYANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalPOWYAPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.powya.base
   pycup.elemental.intrinsic.powya.npa
   pycup.elemental.intrinsic.powya.pca
   pycup.elemental.intrinsic.powya.top
