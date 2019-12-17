pycup.elemental.derived.ax package
==================================

.. automodule:: pycup.elemental.derived.ax
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =====================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.ax.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.ax.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.ax.top.select_engine_class>`  return compatible engine class
  =====================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  =================================  ==============================
  :py:class:`.EngineElementalAX`     Engine class
  :py:class:`.EngineElementalAXNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalAXPca`  Engine class for PyCUDA arrays
  =================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.ax.base
   pycup.elemental.derived.ax.npa
   pycup.elemental.derived.ax.pca
   pycup.elemental.derived.ax.top
