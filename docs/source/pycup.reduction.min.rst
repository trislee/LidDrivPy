pycup.reduction.min package
===========================

.. automodule:: pycup.reduction.min
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.min.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.min.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.min.top.select_engine_class>`  return compatible engine class
  ==============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineReductionMin`     Engine class
  :py:class:`.EngineReductionMinNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionMinPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.min.base
   pycup.reduction.min.npa
   pycup.reduction.min.pca
   pycup.reduction.min.top
