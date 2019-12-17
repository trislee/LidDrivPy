pycup.reduction.amin package
============================

.. automodule:: pycup.reduction.amin
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ===============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.amin.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.amin.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.amin.top.select_engine_class>`  return compatible engine class
  ===============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineReductionAMin`     Engine class
  :py:class:`.EngineReductionAMinNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionAMinPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.amin.base
   pycup.reduction.amin.npa
   pycup.reduction.amin.pca
   pycup.reduction.amin.top
