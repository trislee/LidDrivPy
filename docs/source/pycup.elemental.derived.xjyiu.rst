pycup.elemental.derived.xjyiu package
=====================================

.. automodule:: pycup.elemental.derived.xjyiu
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xjyiu.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xjyiu.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xjyiu.top.select_engine_class>`  return compatible engine class
  ========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalXJYIU`     Engine class
  :py:class:`.EngineElementalXJYIUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXJYIUPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xjyiu.base
   pycup.elemental.derived.xjyiu.npa
   pycup.elemental.derived.xjyiu.pca
   pycup.elemental.derived.xjyiu.top
