pycup.reduction.argamax package
===============================

.. automodule:: pycup.reduction.argamax
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==================================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.argamax.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.argamax.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.argamax.top.select_engine_class>`  return compatible engine class
  ==================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ======================================  ==============================
  :py:class:`.EngineReductionArgamax`     Engine class
  :py:class:`.EngineReductionArgamaxNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionArgamaxPca`  Engine class for PyCUDA arrays
  ======================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.argamax.base
   pycup.reduction.argamax.npa
   pycup.reduction.argamax.pca
   pycup.reduction.argamax.top
