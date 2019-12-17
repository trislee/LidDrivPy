pycup.elemental.derived.xpyfrz package
======================================

.. automodule:: pycup.elemental.derived.xpyfrz
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpyfrz.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpyfrz.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpyfrz.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineElementalXPYFRZ`     Engine class
  :py:class:`.EngineElementalXPYFRZNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPYFRZPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpyfrz.base
   pycup.elemental.derived.xpyfrz.npa
   pycup.elemental.derived.xpyfrz.pca
   pycup.elemental.derived.xpyfrz.top
