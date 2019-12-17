pycup.elemental.derived.xpam2y package
======================================

.. automodule:: pycup.elemental.derived.xpam2y
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpam2y.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpam2y.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpam2y.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =====================================  ==============================
  :py:class:`.EngineElementalXPAM2Y`     Engine class
  :py:class:`.EngineElementalXPAM2YNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPAM2YPca`  Engine class for PyCUDA arrays
  =====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpam2y.base
   pycup.elemental.derived.xpam2y.npa
   pycup.elemental.derived.xpam2y.pca
   pycup.elemental.derived.xpam2y.top
