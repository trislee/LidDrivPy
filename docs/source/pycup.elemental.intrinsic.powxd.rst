pycup.elemental.intrinsic.powxd package
=======================================

.. automodule:: pycup.elemental.intrinsic.powxd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.powxd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.powxd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.powxd.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalPOWXD`     Engine class
  :py:class:`.EngineElementalPOWXDNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalPOWXDPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.powxd.base
   pycup.elemental.intrinsic.powxd.npa
   pycup.elemental.intrinsic.powxd.pca
   pycup.elemental.intrinsic.powxd.top
