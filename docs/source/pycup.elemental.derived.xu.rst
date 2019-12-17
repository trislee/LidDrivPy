pycup.elemental.derived.xu package
==================================

.. automodule:: pycup.elemental.derived.xu
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =====================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xu.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xu.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xu.top.select_engine_class>`  return compatible engine class
  =====================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =================================  ==============================
  :py:class:`.EngineElementalXU`     Engine class
  :py:class:`.EngineElementalXUNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXUPca`  Engine class for PyCUDA arrays
  =================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xu.base
   pycup.elemental.derived.xu.npa
   pycup.elemental.derived.xu.pca
   pycup.elemental.derived.xu.top
