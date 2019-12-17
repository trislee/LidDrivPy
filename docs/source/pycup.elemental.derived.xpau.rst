pycup.elemental.derived.xpau package
====================================

.. automodule:: pycup.elemental.derived.xpau
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpau.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpau.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpau.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalXPAU`     Engine class
  :py:class:`.EngineElementalXPAUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPAUPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpau.base
   pycup.elemental.derived.xpau.npa
   pycup.elemental.derived.xpau.pca
   pycup.elemental.derived.xpau.top
