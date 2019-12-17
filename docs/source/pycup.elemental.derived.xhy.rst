pycup.elemental.derived.xhy package
===================================

.. automodule:: pycup.elemental.derived.xhy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xhy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xhy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xhy.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXHY`     Engine class
  :py:class:`.EngineElementalXHYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXHYPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xhy.base
   pycup.elemental.derived.xhy.npa
   pycup.elemental.derived.xhy.pca
   pycup.elemental.derived.xhy.top
