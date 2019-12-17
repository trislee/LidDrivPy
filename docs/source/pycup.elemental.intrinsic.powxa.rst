pycup.elemental.intrinsic.powxa package
=======================================

.. automodule:: pycup.elemental.intrinsic.powxa
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.powxa.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.powxa.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.powxa.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalPOWXA`     Engine class
  :py:class:`.EngineElementalPOWXANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalPOWXAPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.powxa.base
   pycup.elemental.intrinsic.powxa.npa
   pycup.elemental.intrinsic.powxa.pca
   pycup.elemental.intrinsic.powxa.top
