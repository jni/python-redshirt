import numpy as np
from scipy import ndimage as ndi
from skimage.filters import threshold_otsu


def _extract_roi(image, axis=-1):
    max_frame = np.max(image, axis=axis)
    initial_mask = max_frame > threshold_otsu(max_frame)
    regions = ndi.label(initial_mask)[0]
    region_sizes = np.bincount(np.ravel(regions))
    return regions == (np.argmax(region_sizes[1:]) + 1)


def extract_trace(image, axis=-1):
    """Get a total intensity trace over time out of an image.

    Parameters
    ----------
    image : array
        The input image.
    axis : int, optional
        The axis identifying frames.

    Returns
    -------
    trace : array of float
        The trace of the image data over time.
    roi : array of bool
        The mask used to obtain the trace.
    """
    roi = _extract_roi(image, axis)
    trace = np.sum(image[roi].astype(float), axis=0)
    return trace, roi

