=====
Usage
=====

Examples of conversions:

.. code-block::

    from simplebbox.array import x0y0wh_to_x0y0x1y1, x0y0x1y1_to_x0y0wh

    # convert bbox represented as list in ltwh format:
    x0y0wh_to_x0y0x1y1([100, 200, 10, 20])          # [100, 200, 110, 220]

    # and convert it back:
    x0y0x1y1_to_x0y0wh([100, 200, 110, 220])        # [100, 200, 10, 20]

