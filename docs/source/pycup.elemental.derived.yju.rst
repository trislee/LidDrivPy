pycup.elemental.derived.yju package
===================================

.. automodule:: pycup.elemental.derived.yju
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.yju.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.yju.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.yju.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalYJU`     Engine class
  :py:class:`.EngineElementalYJUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalYJUPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.yju.base
   pycup.elemental.derived.yju.npa
   pycup.elemental.derived.yju.pca
   pycup.elemental.derived.yju.top
