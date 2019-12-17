pycup.elemental.derived.xpa package
===================================

.. automodule:: pycup.elemental.derived.xpa
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpa.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpa.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpa.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXPA`     Engine class
  :py:class:`.EngineElementalXPANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPAPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpa.base
   pycup.elemental.derived.xpa.npa
   pycup.elemental.derived.xpa.pca
   pycup.elemental.derived.xpa.top
