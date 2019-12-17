pycup.elemental.derived.axpy package
====================================

.. automodule:: pycup.elemental.derived.axpy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.axpy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.axpy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.axpy.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalAXPY`     Engine class
  :py:class:`.EngineElementalAXPYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalAXPYPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.axpy.base
   pycup.elemental.derived.axpy.npa
   pycup.elemental.derived.axpy.pca
   pycup.elemental.derived.axpy.top
