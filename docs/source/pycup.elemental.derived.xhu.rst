pycup.elemental.derived.xhu package
===================================

.. automodule:: pycup.elemental.derived.xhu
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xhu.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xhu.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xhu.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXHU`     Engine class
  :py:class:`.EngineElementalXHUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXHUPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xhu.base
   pycup.elemental.derived.xhu.npa
   pycup.elemental.derived.xhu.pca
   pycup.elemental.derived.xhu.top
