pycup.elemental.derived.yz package
==================================

.. automodule:: pycup.elemental.derived.yz
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =====================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.yz.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.yz.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.yz.top.select_engine_class>`  return compatible engine class
  =====================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =================================  ==============================
  :py:class:`.EngineElementalYZ`     Engine class
  :py:class:`.EngineElementalYZNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalYZPca`  Engine class for PyCUDA arrays
  =================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.yz.base
   pycup.elemental.derived.yz.npa
   pycup.elemental.derived.yz.pca
   pycup.elemental.derived.yz.top
