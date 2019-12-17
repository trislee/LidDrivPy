pycup.reduction.bzcc package
============================

.. automodule:: pycup.reduction.bzcc
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ===============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.bzcc.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.bzcc.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.bzcc.top.select_engine_class>`  return compatible engine class
  ===============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineReductionBZcc`     Engine class
  :py:class:`.EngineReductionBZccNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionBZccPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.bzcc.base
   pycup.reduction.bzcc.npa
   pycup.reduction.bzcc.pca
   pycup.reduction.bzcc.top
