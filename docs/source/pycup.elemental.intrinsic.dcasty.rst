pycup.elemental.intrinsic.dcasty package
========================================

.. automodule:: pycup.elemental.intrinsic.dcasty
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ===========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.dcasty.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.dcasty.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.dcasty.top.select_engine_class>`  return compatible engine class
  ===========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineElementalDCASTY`     Engine class
  :py:class:`.EngineElementalDCASTYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalDCASTYPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.dcasty.base
   pycup.elemental.intrinsic.dcasty.npa
   pycup.elemental.intrinsic.dcasty.pca
   pycup.elemental.intrinsic.dcasty.top
