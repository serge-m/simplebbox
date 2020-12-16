==========
SimpleBBox
==========


.. image:: https://img.shields.io/pypi/v/simplebbox.svg
        :target: https://pypi.python.org/pypi/simplebbox

.. image:: https://img.shields.io/travis/serge-m/simplebbox.svg
        :target: https://travis-ci.com/serge-m/simplebbox

.. image:: https://readthedocs.org/projects/simplebbox/badge/?version=latest
        :target: https://simplebbox.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Functions for bounding box processing.

In many computer vision tasks a concept of a bounding box is used. In python bounding boxes are often represented
as lists, tuples or numpy arrays of 4 elements. However there is no standard representation and different formats are used.
Some formats are listed below.

* `(min x, min y, width, height)` or `(left, top, width, height)`
* `(min x, min y, max x, max y)` or `(left, top, bottom, right)`
* `(center x, center y, width, height)`

The coordinates can represent either

* relative position in the image dimensions. Then `x` takes values from `0..1` for pixels inside the image

* or absolute position in pixel


This package contains utility functions to convert between those formats.

Installation
--------------------

.. code-block::

   pip install simplebbox

Usage
--------------------

.. code-block::

    from simplebbox.array import x0y0wh_to_x0y0x1y1, x0y0x1y1_to_x0y0wh

    # convert bbox represented as list in ltwh format:
    x0y0wh_to_x0y0x1y1([100, 200, 10, 20])          # [100, 200, 110, 220]

    # and convert it back:
    x0y0x1y1_to_x0y0wh([100, 200, 110, 220])        # [100, 200, 10, 20]


Notes
--------------------

* Free software: MIT license
* Documentation: https://simplebbox.readthedocs.io.

