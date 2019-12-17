pycup.reduction.sos package
===========================

.. automodule:: pycup.reduction.sos
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.so.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.so.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.so.top.select_engine_class>`  return compatible engine class
  =============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineReductionSos`     Engine class
  :py:class:`.EngineReductionSosNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionSosPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.sos.base
   pycup.reduction.sos.npa
   pycup.reduction.sos.pca
   pycup.reduction.sos.top
