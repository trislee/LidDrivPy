pycup.elemental.intrinsic.minxa package
=======================================

.. automodule:: pycup.elemental.intrinsic.minxa
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.minxa.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.minxa.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.minxa.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalMINXA`     Engine class
  :py:class:`.EngineElementalMINXANpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMINXAPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.minxa.base
   pycup.elemental.intrinsic.minxa.npa
   pycup.elemental.intrinsic.minxa.pca
   pycup.elemental.intrinsic.minxa.top
