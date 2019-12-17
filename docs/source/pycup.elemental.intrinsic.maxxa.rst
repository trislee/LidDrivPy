pycup.elemental.intrinsic.maxxa package
=======================================

.. automodule:: pycup.elemental.intrinsic.maxxa
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.maxxa.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.maxxa.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.maxxa.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalMAXXA`     Engine class
  :py:class:`.EngineElementalMAXXANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMAXXAPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.maxxa.base
   pycup.elemental.intrinsic.maxxa.npa
   pycup.elemental.intrinsic.maxxa.pca
   pycup.elemental.intrinsic.maxxa.top
