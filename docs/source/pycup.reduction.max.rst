pycup.reduction.max package
===========================

.. automodule:: pycup.reduction.max
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.max.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.max.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.max.top.select_engine_class>`  return compatible engine class
  ==============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineReductionMax`     Engine class
  :py:class:`.EngineReductionMaxNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionMaxPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.max.base
   pycup.reduction.max.npa
   pycup.reduction.max.pca
   pycup.reduction.max.top
