pycup.ndops.ndcshift package
============================

.. automodule:: pycup.ndops.ndcshift
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==============================================================================  ==============================
  :py:func:`subroutine() <pycup.ndops.ndcshif.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.ndops.ndcshif.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.ndops.ndcshif.top.select_engine_class>`  return compatible engine class
  ==============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineNdopsNDCSHIFT`     Engine class
  :py:class:`.EngineNdopsNDCSHIFTNpa`  Engine class for NumPy arrays
  :py:class:`.EngineNdopsNDCSHIFTPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.ndops.ndcshift.base
   pycup.ndops.ndcshift.npa
   pycup.ndops.ndcshift.pca
   pycup.ndops.ndcshift.top
