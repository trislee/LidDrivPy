pycup.reduction.nlp package
===========================

.. automodule:: pycup.reduction.nlp
   :members:
   :undoc-members:
   :show-inheritance:

High-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  ==============================================================================  ==============================
  :py:func:`subroutine() <pycup.reduction.nlp.top.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <pycup.reduction.nlp.top.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <pycup.reduction.nlp.top.select_engine_class>`  return compatible engine class
  ==============================================================================  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  ==================================  ==============================
  :py:class:`.EngineReductionNlp`     Engine class
  :py:class:`.EngineReductionNlpNpa`  Engine class for NumPy arrays
  :py:class:`.EngineReductionNlpPca`  Engine class for PyCUDA arrays
  ==================================  ==============================

Submodules
----------

.. toctree::

   pycup.reduction.nlp.base
   pycup.reduction.nlp.npa
   pycup.reduction.nlp.pca
   pycup.reduction.nlp.top
