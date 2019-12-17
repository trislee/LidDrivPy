pycup.elemental.derived.mxpa package
====================================

.. automodule:: pycup.elemental.derived.mxpa
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.mxpa.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.mxpa.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.mxpa.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalMXPA`     Engine class
  :py:class:`.EngineElementalMXPANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMXPAPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.mxpa.base
   pycup.elemental.derived.mxpa.npa
   pycup.elemental.derived.mxpa.pca
   pycup.elemental.derived.mxpa.top
