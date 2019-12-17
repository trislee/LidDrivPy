pycup.reduction.sum package
===========================

.. automodule:: pycup.reduction.sum
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.sum.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.sum.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.sum.top.select_engine_class>`  return compatible engine class
  ==============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineReductionSum`     Engine class
  :py:class:`.EngineReductionSumNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionSumPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.sum.base
   pycup.reduction.sum.npa
   pycup.reduction.sum.pca
   pycup.reduction.sum.top
