pycup.elemental.derived.myu package
===================================

.. automodule:: pycup.elemental.derived.myu
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.myu.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.myu.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.myu.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalMYU`     Engine class
  :py:class:`.EngineElementalMYUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMYUPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.myu.base
   pycup.elemental.derived.myu.npa
   pycup.elemental.derived.myu.pca
   pycup.elemental.derived.myu.top
