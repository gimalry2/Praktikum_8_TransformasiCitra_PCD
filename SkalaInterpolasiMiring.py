# Mengimpor pustaka
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("orange.jpg") # Membaca gambar
fig, ax = plt.subplots(1, 3, figsize=(16, 8)) # Inisialisasi figure dan axes

# Scaling gambar dengan interpolasi linier
image_scaled = cv.resize(image, None, fx=0.15, fy=0.15)  # Penskalaan dengan faktor 0.15
ax[0].imshow(cv.cvtColor(image_scaled, cv.COLOR_BGR2RGB))  # Menampilkan gambar hasil scaling
ax[0].set_title("Linear Interpolation Scale")  # Menetapkan judul untuk axes pertama

# Scaling gambar dengan interpolasi kubik
image_scaled_2 = cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)  # Penskalaan dengan faktor 2 dan metode INTER_CUBIC
ax[1].imshow(cv.cvtColor(image_scaled_2, cv.COLOR_BGR2RGB))  # Menampilkan gambar hasil scaling
ax[1].set_title("Cubic Interpolation Scale")  # Menetapkan judul untuk axes kedua

# Scaling gambar dengan eksplisit dan metode interpolasi AREA
image_scaled_3 = cv.resize(image, (200, 400), interpolation=cv.INTER_AREA)  # Penskalaan ke ukuran 200x400 dengan metode INTER_AREA
ax[2].imshow(cv.cvtColor(image_scaled_3, cv.COLOR_BGR2RGB))  # Menampilkan gambar hasil scaling
ax[2].set_title("Skewed Interpolation Scale")  # Menetapkan judul untuk axes ketiga

plt.show()  # Menampilkan gambar 