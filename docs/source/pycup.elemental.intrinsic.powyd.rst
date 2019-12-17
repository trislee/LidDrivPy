pycup.elemental.intrinsic.powyd package
=======================================

.. automodule:: pycup.elemental.intrinsic.powyd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.powyd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.powyd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.powyd.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalPOWYD`     Engine class
  :py:class:`.EngineElementalPOWYDNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalPOWYDPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.powyd.base
   pycup.elemental.intrinsic.powyd.npa
   pycup.elemental.intrinsic.powyd.pca
   pycup.elemental.intrinsic.powyd.top
