pycup.elemental.derived.dy package
==================================

.. automodule:: pycup.elemental.derived.dy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =====================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.dy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.dy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.dy.top.select_engine_class>`  return compatible engine class
  =====================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =================================  ==============================
  :py:class:`.EngineElementalDY`     Engine class
  :py:class:`.EngineElementalDYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalDYPca`  Engine class for PyCUDA arrays
  =================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.dy.base
   pycup.elemental.derived.dy.npa
   pycup.elemental.derived.dy.pca
   pycup.elemental.derived.dy.top
