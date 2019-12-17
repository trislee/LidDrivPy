pycup.reduction.dot package
===========================

.. automodule:: pycup.reduction.dot
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.do.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.do.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.do.top.select_engine_class>`  return compatible engine class
  =============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineReductionDot`     Engine class
  :py:class:`.EngineReductionDotNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionDotPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.dot.base
   pycup.reduction.dot.npa
   pycup.reduction.dot.pca
   pycup.reduction.dot.top
