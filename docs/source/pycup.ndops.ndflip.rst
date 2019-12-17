pycup.ndops.ndflip package
==========================

.. automodule:: pycup.ndops.ndflip
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =============================================================================  ==============================
  :py:func:`subroutine() <pycup.ndops.ndflip.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.ndops.ndflip.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.ndops.ndflip.top.select_engine_class>`  return compatible engine class
  =============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =================================  ==============================
  :py:class:`.EngineNdopsNDFLIP`     Engine class
  :py:class:`.EngineNdopsNDFLIPNpa`  Engine class for NumPy arrays
  :py:class:`.EngineNdopsNDFLIPPca`  Engine class for PyCUDA arrays
  =================================  ==============================

Submodules
----------

.. toctree::

   pycup.ndops.ndflip.base
   pycup.ndops.ndflip.npa
   pycup.ndops.ndflip.pca
   pycup.ndops.ndflip.top
