pycup.elemental.intrinsic.minxd package
=======================================

.. automodule:: pycup.elemental.intrinsic.minxd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.minxd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.minxd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.minxd.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalMINXD`     Engine class
  :py:class:`.EngineElementalMINXDNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMINXDPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.minxd.base
   pycup.elemental.intrinsic.minxd.npa
   pycup.elemental.intrinsic.minxd.pca
   pycup.elemental.intrinsic.minxd.top
