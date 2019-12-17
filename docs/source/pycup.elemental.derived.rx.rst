pycup.elemental.derived.rx package
==================================

.. automodule:: pycup.elemental.derived.rx
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =====================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.rx.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.rx.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.rx.top.select_engine_class>`  return compatible engine class
  =====================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =================================  ==============================
  :py:class:`.EngineElementalRX`     Engine class
  :py:class:`.EngineElementalRXNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalRXPca`  Engine class for PyCUDA arrays
  =================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.rx.base
   pycup.elemental.derived.rx.npa
   pycup.elemental.derived.rx.pca
   pycup.elemental.derived.rx.top
