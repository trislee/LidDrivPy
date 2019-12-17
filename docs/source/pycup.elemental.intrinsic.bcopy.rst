pycup.elemental.intrinsic.bcopy package
=======================================

.. automodule:: pycup.elemental.intrinsic.bcopy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.bcopy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.bcopy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.bcopy.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalBCOPY`     Engine class
  :py:class:`.EngineElementalBCOPYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalBCOPYPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.bcopy.base
   pycup.elemental.intrinsic.bcopy.npa
   pycup.elemental.intrinsic.bcopy.pca
   pycup.elemental.intrinsic.bcopy.top
