pycup.ndops.ndvcshift package
=============================

.. automodule:: pycup.ndops.ndvcshift
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ===============================================================================  ==============================
  :py:func:`subroutine() <pycup.ndops.ndvcshif.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.ndops.ndvcshif.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.ndops.ndvcshif.top.select_engine_class>`  return compatible engine class
  ===============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineNdopsNDVCSHIFT`     Engine class
  :py:class:`.EngineNdopsNDVCSHIFTNpa`  Engine class for NumPy arrays
  :py:class:`.EngineNdopsNDVCSHIFTPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.ndops.ndvcshift.base
   pycup.ndops.ndvcshift.npa
   pycup.ndops.ndvcshift.pca
   pycup.ndops.ndvcshift.top
