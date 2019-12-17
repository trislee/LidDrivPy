pycup.elemental.derived.ppxpa package
=====================================

.. automodule:: pycup.elemental.derived.ppxpa
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.ppxpa.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.ppxpa.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.ppxpa.top.select_engine_class>`  return compatible engine class
  ========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalPPXPA`     Engine class
  :py:class:`.EngineElementalPPXPANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalPPXPAPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.ppxpa.base
   pycup.elemental.derived.ppxpa.npa
   pycup.elemental.derived.ppxpa.pca
   pycup.elemental.derived.ppxpa.top
