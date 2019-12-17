pycup.elemental.derived.xjyu package
====================================

.. automodule:: pycup.elemental.derived.xjyu
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xjyu.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xjyu.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xjyu.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalXJYU`     Engine class
  :py:class:`.EngineElementalXJYUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXJYUPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xjyu.base
   pycup.elemental.derived.xjyu.npa
   pycup.elemental.derived.xjyu.pca
   pycup.elemental.derived.xjyu.top
