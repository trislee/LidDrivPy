pycup.reduction.nl1 package
===========================

.. automodule:: pycup.reduction.nl1
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.nl1.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.nl1.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.nl1.top.select_engine_class>`  return compatible engine class
  ==============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineReductionNl1`     Engine class
  :py:class:`.EngineReductionNl1Npa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionNl1Pca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.nl1.base
   pycup.reduction.nl1.npa
   pycup.reduction.nl1.pca
   pycup.reduction.nl1.top
