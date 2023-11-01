from rasterio.plot import show
import rasterio
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

composite = rasterio.open(r"E:\Saniha\DIP\Landset\rgb.tif")
show(composite)
plt.show()
plt.title("color composite")