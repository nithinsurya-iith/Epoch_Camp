from PIL import Image
from matplotlib import pyplot
import numpy as np

im_g = np.array(Image.open('img.png').convert('L'))
im = np.array(Image.open('img.png'))

im_g_trm = im_g[0:im_g.shape[0]//2, 0:im_g.shape[1]//2]
img_g_top = np.hstack((im_g_trm,np.flip(im_g_trm,1)))
img_g_bot = np.flip(img_g_top,0)
img_g = np.vstack((img_g_top,img_g_bot))

im_trm = im[0:im.shape[0]//2, 0:im.shape[1]//2]
img_top = np.hstack((im_trm,np.flip(im_trm,1)))
img_bot = np.flip(img_top,0)
img = np.vstack((img_top,img_bot))

fig, ax = pyplot.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(img_g,cmap='gray')
ax[0].axis("off")  # Hide axis
ax[0].set_title("Image 1")

ax[1].imshow(img)
ax[1].axis("off")
ax[1].set_title("Image 2")

pyplot.show()
