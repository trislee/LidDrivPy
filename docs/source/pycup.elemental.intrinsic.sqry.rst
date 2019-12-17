pycup.elemental.intrinsic.sqry package
======================================

.. automodule:: pycup.elemental.intrinsic.sqry
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.sqry.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.sqry.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.sqry.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalSQRY`     Engine class
  :py:class:`.EngineElementalSQRYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalSQRYPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.sqry.base
   pycup.elemental.intrinsic.sqry.npa
   pycup.elemental.intrinsic.sqry.pca
   pycup.elemental.intrinsic.sqry.top
