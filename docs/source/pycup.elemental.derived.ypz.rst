pycup.elemental.derived.ypz package
===================================

.. automodule:: pycup.elemental.derived.ypz
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.ypz.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.ypz.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.ypz.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalYPZ`     Engine class
  :py:class:`.EngineElementalYPZNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalYPZPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.ypz.base
   pycup.elemental.derived.ypz.npa
   pycup.elemental.derived.ypz.pca
   pycup.elemental.derived.ypz.top
