pycup.reduction.bdot package
============================

.. automodule:: pycup.reduction.bdot
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.bdo.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.bdo.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.bdo.top.select_engine_class>`  return compatible engine class
  ==============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineReductionBDot`     Engine class
  :py:class:`.EngineReductionBDotNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionBDotPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.bdot.base
   pycup.reduction.bdot.npa
   pycup.reduction.bdot.pca
   pycup.reduction.bdot.top
