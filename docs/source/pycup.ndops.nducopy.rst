pycup.ndops.nducopy package
===========================

.. automodule:: pycup.ndops.nducopy
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==============================================================================  ==============================
  :py:func:`subroutine() <pycup.ndops.nducopy.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.ndops.nducopy.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.ndops.nducopy.top.select_engine_class>`  return compatible engine class
  ==============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineNdopsNDUCOPY`     Engine class
  :py:class:`.EngineNdopsNDUCOPYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineNdopsNDUCOPYPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.ndops.nducopy.base
   pycup.ndops.nducopy.npa
   pycup.ndops.nducopy.pca
   pycup.ndops.nducopy.top
