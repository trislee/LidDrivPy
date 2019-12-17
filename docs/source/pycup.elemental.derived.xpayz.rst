pycup.elemental.derived.xpayz package
=====================================

.. automodule:: pycup.elemental.derived.xpayz
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpayz.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpayz.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpayz.top.select_engine_class>`  return compatible engine class
  ========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalXPAYZ`     Engine class
  :py:class:`.EngineElementalXPAYZNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPAYZPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpayz.base
   pycup.elemental.derived.xpayz.npa
   pycup.elemental.derived.xpayz.pca
   pycup.elemental.derived.xpayz.top
