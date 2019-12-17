pycup.elemental.intrinsic.sqrty package
=======================================

.. automodule:: pycup.elemental.intrinsic.sqrty
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.sqrty.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.sqrty.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.sqrty.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalSQRTY`     Engine class
  :py:class:`.EngineElementalSQRTYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalSQRTYPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.sqrty.base
   pycup.elemental.intrinsic.sqrty.npa
   pycup.elemental.intrinsic.sqrty.pca
   pycup.elemental.intrinsic.sqrty.top
