pycup.elemental.derived.xiu package
===================================

.. automodule:: pycup.elemental.derived.xiu
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xiu.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xiu.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xiu.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXIU`     Engine class
  :py:class:`.EngineElementalXIUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXIUPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xiu.base
   pycup.elemental.derived.xiu.npa
   pycup.elemental.derived.xiu.pca
   pycup.elemental.derived.xiu.top
