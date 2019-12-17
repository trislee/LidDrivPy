pycup.elemental.derived.dx package
==================================

.. automodule:: pycup.elemental.derived.dx
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =====================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.dx.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.dx.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.dx.top.select_engine_class>`  return compatible engine class
  =====================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =================================  ==============================
  :py:class:`.EngineElementalDX`     Engine class
  :py:class:`.EngineElementalDXNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalDXPca`  Engine class for PyCUDA arrays
  =================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.dx.base
   pycup.elemental.derived.dx.npa
   pycup.elemental.derived.dx.pca
   pycup.elemental.derived.dx.top
