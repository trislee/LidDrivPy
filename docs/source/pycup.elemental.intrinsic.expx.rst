pycup.elemental.intrinsic.expx package
======================================

.. automodule:: pycup.elemental.intrinsic.expx
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.expx.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.expx.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.expx.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalEXPX`     Engine class
  :py:class:`.EngineElementalEXPXNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalEXPXPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.expx.base
   pycup.elemental.intrinsic.expx.npa
   pycup.elemental.intrinsic.expx.pca
   pycup.elemental.intrinsic.expx.top
