pycup.elemental.derived.m2yz package
====================================

.. automodule:: pycup.elemental.derived.m2yz
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.m2yz.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.m2yz.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.m2yz.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalM2YZ`     Engine class
  :py:class:`.EngineElementalM2YZNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalM2YZPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.m2yz.base
   pycup.elemental.derived.m2yz.npa
   pycup.elemental.derived.m2yz.pca
   pycup.elemental.derived.m2yz.top
