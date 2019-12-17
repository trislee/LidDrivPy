pycup.reduction.argmax package
==============================

.. automodule:: pycup.reduction.argmax
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =================================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.argmax.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.argmax.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.argmax.top.select_engine_class>`  return compatible engine class
  =================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineReductionArgmax`     Engine class
  :py:class:`.EngineReductionArgmaxNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionArgmaxPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.argmax.base
   pycup.reduction.argmax.npa
   pycup.reduction.argmax.pca
   pycup.reduction.argmax.top
