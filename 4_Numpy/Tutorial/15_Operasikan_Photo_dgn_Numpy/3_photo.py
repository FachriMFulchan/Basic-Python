#dengan numpy juga kita bisa mengoperasikan photo
import numpy as np
import matplotlib.pyplot as plt
from skimage import io


photo = io.imread('nature.jpg')
print (type(photo)) #numpy array loh jenisnya
print(np.shape(photo))

# plt.imshow(photo[::-1]) #ngebalikin keatas
# plt.imshow(photo[:,::-1]) #di mirror
# plt.imshow(photo[250:900,1900:3200]) #baris,kolom

# photo_sin = np.sin(photo)
# print (photo_sin)

# print(np.sum(photo))
# print(np.prod(photo))
# print(np.mean(photo))
# print(np.std(photo))
# print(np.var(photo))
# print(np.min(photo))
# print(np.max(photo))
# print(np.argmin(photo))
# print (np.argmax(photo))

photo_masked = np.where(photo > 100,255,0) #kode warna RGB nya
plt.imshow(photo_masked)

# plt.imshow(photo[:,:,0].T)

plt.show()