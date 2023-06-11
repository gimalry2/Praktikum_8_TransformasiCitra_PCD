# Mengimpor pustaka
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("dog.jfif") # Membaca gambar dengan OpenCV
h, w = image.shape[:2] # Tinggi (h) dan lebar (w)

# Membuat matriks rotasi dengan menggunakan titik tengah gambar, sudut rotasi -180 derajat, dan skala 0.5
rotation_matrix = cv.getRotationMatrix2D((w/2, h/2), -180, 0.5)

# Melakukan transformasi rotasi pada gambar menggunakan matriks rotasi
rotated_image = cv.warpAffine(image, rotation_matrix, (w, h))

# Menampilkan gambar yang sudah dirotasi menggunakan Matplotlib
plt.imshow(cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB))
plt.title("Rotation")
plt.show()
