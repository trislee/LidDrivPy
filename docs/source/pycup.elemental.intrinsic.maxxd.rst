pycup.elemental.intrinsic.maxxd package
=======================================

.. automodule:: pycup.elemental.intrinsic.maxxd
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==========================================================================================  ==============================
  :py:func:`subroutine() <pycup.elemental.intrinsic.maxxd.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.elemental.intrinsic.maxxd.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.elemental.intrinsic.maxxd.top.select_engine_class>`  return compatible engine class
  ==========================================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ====================================  ==============================
  :py:class:`.EngineElementalMAXXD`     Engine class
  :py:class:`.EngineElementalMAXXDNpa`  Engine class for NumPy arrays
  :py:class:`.EngineElementalMAXXDPca`  Engine class for PyCUDA arrays
  ====================================  ==============================

Submodules
----------

.. toctree::

   pycup.elemental.intrinsic.maxxd.base
   pycup.elemental.intrinsic.maxxd.npa
   pycup.elemental.intrinsic.maxxd.pca
   pycup.elemental.intrinsic.maxxd.top
