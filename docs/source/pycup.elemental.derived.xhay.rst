pycup.elemental.derived.xhay package
====================================

.. automodule:: pycup.elemental.derived.xhay
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xhay.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xhay.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xhay.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalXHAY`     Engine class
  :py:class:`.EngineElementalXHAYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXHAYPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xhay.base
   pycup.elemental.derived.xhay.npa
   pycup.elemental.derived.xhay.pca
   pycup.elemental.derived.xhay.top
