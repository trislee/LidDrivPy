pycup.elemental.derived.xywd package
====================================

.. automodule:: pycup.elemental.derived.xywd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xywd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xywd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xywd.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalXYWD`     Engine class
  :py:class:`.EngineElementalXYWDNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXYWDPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xywd.base
   pycup.elemental.derived.xywd.npa
   pycup.elemental.derived.xywd.pca
   pycup.elemental.derived.xywd.top
