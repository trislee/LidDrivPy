pycup.reduction.argmin package
==============================

.. automodule:: pycup.reduction.argmin
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =================================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.argmin.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.argmin.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.argmin.top.select_engine_class>`  return compatible engine class
  =================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineReductionArgmin`     Engine class
  :py:class:`.EngineReductionArgminNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionArgminPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.argmin.base
   pycup.reduction.argmin.npa
   pycup.reduction.argmin.pca
   pycup.reduction.argmin.top
