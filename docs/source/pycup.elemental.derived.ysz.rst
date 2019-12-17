pycup.elemental.derived.ysz package
===================================

.. automodule:: pycup.elemental.derived.ysz
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.ysz.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.ysz.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.ysz.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalYSZ`     Engine class
  :py:class:`.EngineElementalYSZNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalYSZPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.ysz.base
   pycup.elemental.derived.ysz.npa
   pycup.elemental.derived.ysz.pca
   pycup.elemental.derived.ysz.top
