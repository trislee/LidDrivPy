pycup.elemental.intrinsic.ucasty package
========================================

.. automodule:: pycup.elemental.intrinsic.ucasty
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ===========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.ucasty.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.ucasty.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.ucasty.top.select_engine_class>`  return compatible engine class
  ===========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineElementalUCASTY`     Engine class
  :py:class:`.EngineElementalUCASTYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalUCASTYPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.ucasty.base
   pycup.elemental.intrinsic.ucasty.npa
   pycup.elemental.intrinsic.ucasty.pca
   pycup.elemental.intrinsic.ucasty.top
