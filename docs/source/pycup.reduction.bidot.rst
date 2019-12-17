pycup.reduction.bidot package
=============================

.. automodule:: pycup.reduction.bidot
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ===============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.bido.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.bido.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.bido.top.select_engine_class>`  return compatible engine class
  ===============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineReductionBidot`     Engine class
  :py:class:`.EngineReductionBidotNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionBidotPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.bidot.base
   pycup.reduction.bidot.npa
   pycup.reduction.bidot.pca
   pycup.reduction.bidot.top
