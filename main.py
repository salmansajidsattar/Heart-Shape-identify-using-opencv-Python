from stl_tools import numpy2stl
from pylab import imread
#from scipy.misc import lena, imresize
from scipy.ndimage import gaussian_filter

#
# A = imresize(lena(), (256, 256))  # load Lena image, shrink in half
# A = gaussian_filter(A, 1)  # smoothing
#
# numpy2stl(A, "examples/Lena.stl", scale=0.1, solid=False)



A = 256 * imread("apple.png")
A = A[:, :, 2] + 1.0*A[:,:, 0] # Compose RGBA channels to give depth
A = gaussian_filter(A, 1)  # smoothing
numpy2stl(A, "NASA.stl", scale=0.05, mask_val=5., solid=True)