# python-redshirt

Read Redshirt camera format data into NumPy arrays

The format is described in
[this page](http://www.redshirtimaging.com/support/dfo.html).

This library was written to fulfill a very specific need so initially
we only support CCD/CMOS camera data.

The file contains uncompressed 16-bit integer data in the following order:

- a header (2560 ints)
- image data (80 x 80 x nframes pixels, in C-order)
- BNC recording data (8 x nframes, C-order)
- blank (background) image (80 x 80)
- 8 pixels (???)
