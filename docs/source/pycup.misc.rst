pycup.misc package
==================

.. automodule:: pycup.misc
   :members:
   :undoc-members:
   :show-inheritance:

Subpackages
-----------

.. toctree::
   :maxdepth: 1

   pycup.misc.ndpad

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  =====================================================================  ==============================
  :py:func:`subroutine() <pycup.misc.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.misc.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.misc.top.select_engine_class>`  return compatible engine class
  =====================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==============================  ==============================
  :py:class:`.EngineMiscMISC`     Engine class
  :py:class:`.EngineMiscMISCNpa`  Engine class for NumPy arrays
  :py:class:`.EngineMiscMISCPca`  Engine class for PyCUDA arrays
  ==============================  ==============================

Submodules
----------

.. toctree::

   pycup.misc.base
   pycup.misc.npa
   pycup.misc.pca
