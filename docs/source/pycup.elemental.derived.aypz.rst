pycup.elemental.derived.aypz package
====================================

.. automodule:: pycup.elemental.derived.aypz
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.aypz.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.aypz.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.aypz.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalAYPZ`     Engine class
  :py:class:`.EngineElementalAYPZNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalAYPZPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.aypz.base
   pycup.elemental.derived.aypz.npa
   pycup.elemental.derived.aypz.pca
   pycup.elemental.derived.aypz.top
