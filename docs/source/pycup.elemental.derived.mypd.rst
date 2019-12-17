pycup.elemental.derived.mypd package
====================================

.. automodule:: pycup.elemental.derived.mypd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.mypd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.mypd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.mypd.top.select_engine_class>`  return compatible engine class
  =======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===================================  ==============================
  :py:class:`.EngineElementalMYPD`     Engine class
  :py:class:`.EngineElementalMYPDNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMYPDPca`  Engine class for PyCUDA arrays
  ===================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.mypd.base
   pycup.elemental.derived.mypd.npa
   pycup.elemental.derived.mypd.pca
   pycup.elemental.derived.mypd.top
