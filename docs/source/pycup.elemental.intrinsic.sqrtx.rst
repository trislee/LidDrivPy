pycup.elemental.intrinsic.sqrtx package
=======================================

.. automodule:: pycup.elemental.intrinsic.sqrtx
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.sqrtx.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.sqrtx.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.sqrtx.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalSQRTX`     Engine class
  :py:class:`.EngineElementalSQRTXNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalSQRTXPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.sqrtx.base
   pycup.elemental.intrinsic.sqrtx.npa
   pycup.elemental.intrinsic.sqrtx.pca
   pycup.elemental.intrinsic.sqrtx.top
