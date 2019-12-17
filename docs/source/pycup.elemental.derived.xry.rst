pycup.elemental.derived.xry package
===================================

.. automodule:: pycup.elemental.derived.xry
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xry.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xry.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xry.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXRY`     Engine class
  :py:class:`.EngineElementalXRYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXRYPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xry.base
   pycup.elemental.derived.xry.npa
   pycup.elemental.derived.xry.pca
   pycup.elemental.derived.xry.top
