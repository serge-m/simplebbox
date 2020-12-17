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

* or absolute position in pixel (either integer or floating point numbers)


This package contains utility functions to convert between those formats.


Basic assumptions
---------------------

Simple data structures are used: lists, tuples, numpy arrays. They fit well to the output of the deep learning models.
Speed and simplicity is chosen over type and range safety. For better type safety one can use alternative implementations with
classes. See `alternatives` page of the docs.

Conversion operations between integer and float numbers are sometimes cumbersome. We are trying to keep it aligned
with standard python. For example rounding of float numbers while computing a center of a bounding box is done using
`Round_half_to_even`_ algorithm.

Several functions for different handing of floats/ints are provided for the same operation.
E.g. `cxcywh_to_x0y0wh_float`, `cxcywh_to_x0y0wh_int`

In simple use cases like a single conversion from one format to another one can probably chose any of the versions for
float conversions. More thorough selection is needed in case of multiple back and forth conversions.

.. _Round_half_to_even: https://en.wikipedia.org/wiki/Rounding#Round_half_to_even

Installation
--------------------

.. code-block::

   pip install simplebbox


Usage example
--------------------

Examples of conversions:

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

