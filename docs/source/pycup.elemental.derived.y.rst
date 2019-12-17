pycup.elemental.derived.y package
=================================

.. automodule:: pycup.elemental.derived.y
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ====================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.y.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.y.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.y.top.select_engine_class>`  return compatible engine class
  ====================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ================================  ==============================
  :py:class:`.EngineElementalY`     Engine class
  :py:class:`.EngineElementalYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalYPca`  Engine class for PyCUDA arrays
  ================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.y.base
   pycup.elemental.derived.y.npa
   pycup.elemental.derived.y.pca
   pycup.elemental.derived.y.top
