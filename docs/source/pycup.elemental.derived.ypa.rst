pycup.elemental.derived.ypa package
===================================

.. automodule:: pycup.elemental.derived.ypa
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.ypa.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.ypa.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.ypa.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalYPA`     Engine class
  :py:class:`.EngineElementalYPANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalYPAPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.ypa.base
   pycup.elemental.derived.ypa.npa
   pycup.elemental.derived.ypa.pca
   pycup.elemental.derived.ypa.top
