pycup.elemental.derived.xiy package
===================================

.. automodule:: pycup.elemental.derived.xiy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xiy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xiy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xiy.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXIY`     Engine class
  :py:class:`.EngineElementalXIYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXIYPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xiy.base
   pycup.elemental.derived.xiy.npa
   pycup.elemental.derived.xiy.pca
   pycup.elemental.derived.xiy.top
