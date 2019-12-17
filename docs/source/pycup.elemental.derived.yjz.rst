pycup.elemental.derived.yjz package
===================================

.. automodule:: pycup.elemental.derived.yjz
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.yjz.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.yjz.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.yjz.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalYJZ`     Engine class
  :py:class:`.EngineElementalYJZNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalYJZPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.yjz.base
   pycup.elemental.derived.yjz.npa
   pycup.elemental.derived.yjz.pca
   pycup.elemental.derived.yjz.top
