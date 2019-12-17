pycup.elemental.derived.ypau package
====================================

.. automodule:: pycup.elemental.derived.ypau
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.ypau.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.ypau.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.ypau.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalYPAU`     Engine class
  :py:class:`.EngineElementalYPAUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalYPAUPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.ypau.base
   pycup.elemental.derived.ypau.npa
   pycup.elemental.derived.ypau.pca
   pycup.elemental.derived.ypau.top
