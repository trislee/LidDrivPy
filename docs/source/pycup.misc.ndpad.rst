pycup.misc.ndpad package
========================

.. automodule:: pycup.misc.ndpad
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ===========================================================================  ==============================
  :py:func:`subroutine() <pycup.misc.ndpad.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.misc.ndpad.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.misc.ndpad.top.select_engine_class>`  return compatible engine class
  ===========================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ===============================  ==============================
  :py:class:`.EngineMiscNDPAD`     Engine class
  :py:class:`.EngineMiscNDPADNpa`  Engine class for NumPy arrays
  :py:class:`.EngineMiscNDPADPca`  Engine class for PyCUDA arrays
  ===============================  ==============================

Submodules
----------

.. toctree::

   pycup.misc.ndpad.base
   pycup.misc.ndpad.npa
   pycup.misc.ndpad.pca
   pycup.misc.ndpad.top
