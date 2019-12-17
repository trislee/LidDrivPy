pycup.elemental.derived.mxpafry package
=======================================

.. automodule:: pycup.elemental.derived.mxpafry
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.derived.mxpafry.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.derived.mxpafry.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.derived.mxpafry.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ======================================  ==============================
  :py:class:`.EngineElementalMXPAFRY`     Engine class
  :py:class:`.EngineElementalMXPAFRYNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMXPAFRYPca`  Engine class for PyCUDA arrays
  ======================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.derived.mxpafry.base
   pycup.elemental.derived.mxpafry.npa
   pycup.elemental.derived.mxpafry.pca
   pycup.elemental.derived.mxpafry.top
