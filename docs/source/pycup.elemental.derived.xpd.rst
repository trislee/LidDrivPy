pycup.elemental.derived.xpd package
===================================

.. automodule:: pycup.elemental.derived.xpd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ======================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.xpd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.xpd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.xpd.top.select_engine_class>`  return compatible engine class
  ======================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineElementalXPD`     Engine class
  :py:class:`.EngineElementalXPDNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalXPDPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.xpd.base
   pycup.elemental.derived.xpd.npa
   pycup.elemental.derived.xpd.pca
   pycup.elemental.derived.xpd.top
