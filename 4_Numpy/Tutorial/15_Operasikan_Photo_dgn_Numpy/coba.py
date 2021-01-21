import numpy as np
import matplotlib.pyplot as plt
from skimage import io

photo = io.imread('nature.jpg')
# plt.imshow(photo)
print (type(photo))
# print(np.shape(photo))

#mirror
# plt.imshow(photo[:,::-1])

#balikkin atas bawah
# plt.imshow(photo[::-1,:])

#transpose
# plt.imshow(photo[::-1,:,0].T)

# #slicing
# plt.imshow(photo[250:900,1900:3200])

#masking sederhana
# photo_mask = np.where(photo > 100, 255, 0)
# plt.imshow(photo_mask)



plt.show()
