.. _api:

API Reference
=============

This page provides an auto-generated summary of Xoak's API.

.. currentmodule:: xoak

Xarray NDPointIndex tree adapters
---------------------------------

The following classes may be used with :py:class:`xarray.indexes.NDPointIndex`, they can
be passed as ``tree_adapter_cls`` option value via :py:meth:`xarray.Dataset.set_xindex` or
:py:meth:`xarray.DataArray.set_xindex`.

.. autosummary::
   :toctree: _api_generated/

    S2PointTreeAdapter
    SklearnBallTreeAdapter
    SklearnGeoBallTreeAdapter
    SklearnKDTreeAdapter

.. currentmodule:: xarray

Dataset.xoak
------------

.. warning::

   This API is deprecated and will be removed in a future version of Xoak.

This accessor extends :py:class:`xarray.Dataset` with all the methods and
properties listed below. Proper use of this accessor should be like:

.. code-block:: python

   >>> import xarray as xr         # first import xarray
   >>> import xoak                 # import xoak (the 'xoak' accessor is registered)
   >>> ds = xr.Dataset()           # create or load an xarray Dataset
   >>> ds.xoak.<meth_or_prop>      # access to the methods and properties listed below

**Properties**

.. autosummary::
   :toctree: _api_generated/
   :template: autosummary/accessor_attribute.rst

   Dataset.xoak.index

**Methods**

.. autosummary::
   :toctree: _api_generated/
   :template: autosummary/accessor_method.rst

    Dataset.xoak.set_index
    Dataset.xoak.sel

DataArray.xoak
--------------

.. warning::

   This API is deprecated and will be removed in a future version of Xoak.

The accessor above is also registered for :py:class:`xarray.DataArray`.

**Properties**

.. autosummary::
   :toctree: _api_generated/
   :template: autosummary/accessor_attribute.rst

   DataArray.xoak.index

**Methods**

.. autosummary::
   :toctree: _api_generated/
   :template: autosummary/accessor_method.rst

    DataArray.xoak.set_index
    DataArray.xoak.sel
