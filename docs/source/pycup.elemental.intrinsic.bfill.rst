pycup.elemental.intrinsic.bfill package
=======================================

.. automodule:: pycup.elemental.intrinsic.bfill
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.bfill.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.bfill.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.bfill.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalBFILL`     Engine class
  :py:class:`.EngineElementalBFILLNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalBFILLPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.bfill.base
   pycup.elemental.intrinsic.bfill.npa
   pycup.elemental.intrinsic.bfill.pca
   pycup.elemental.intrinsic.bfill.top
