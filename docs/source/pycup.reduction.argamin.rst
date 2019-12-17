pycup.reduction.argamin package
===============================

.. automodule:: pycup.reduction.argamin
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==================================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.argamin.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.argamin.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.argamin.top.select_engine_class>`  return compatible engine class
  ==================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ======================================  ==============================
  :py:class:`.EngineReductionArgamin`     Engine class
  :py:class:`.EngineReductionArgaminNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionArgaminPca`  Engine class for PyCUDA arrays
  ======================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.argamin.base
   pycup.reduction.argamin.npa
   pycup.reduction.argamin.pca
   pycup.reduction.argamin.top
