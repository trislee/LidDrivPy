pycup.reduction.amax package
============================

.. automodule:: pycup.reduction.amax
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ===============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.amax.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.amax.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.amax.top.select_engine_class>`  return compatible engine class
  ===============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineReductionAMax`     Engine class
  :py:class:`.EngineReductionAMaxNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionAMaxPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.amax.base
   pycup.reduction.amax.npa
   pycup.reduction.amax.pca
   pycup.reduction.amax.top
