pycup.elemental.derived.xpay package
====================================

.. automodule:: pycup.elemental.derived.xpay
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpay.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpay.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpay.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalXPAY`     Engine class
  :py:class:`.EngineElementalXPAYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPAYPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpay.base
   pycup.elemental.derived.xpay.npa
   pycup.elemental.derived.xpay.pca
   pycup.elemental.derived.xpay.top
