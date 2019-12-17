pycup.elemental.intrinsic.sqrx package
======================================

.. automodule:: pycup.elemental.intrinsic.sqrx
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.sqrx.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.sqrx.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.sqrx.top.select_engine_class>`  return compatible engine class
  =========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalSQRX`     Engine class
  :py:class:`.EngineElementalSQRXNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalSQRXPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.sqrx.base
   pycup.elemental.intrinsic.sqrx.npa
   pycup.elemental.intrinsic.sqrx.pca
   pycup.elemental.intrinsic.sqrx.top
