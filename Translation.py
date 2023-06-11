# Mengimpor pustaka
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


image = cv.imread("orange.jpg") # Membaca gambar
h, w = image.shape[:2] # Tinggi (h) dan lebar (w) 
half_height, half_width = h // 4, w // 8 # Menghitung setengah tinggi dan setengah lebar
transition_matrix = np.float32([[1, 0, half_width], [0, 1, half_height]]) # Membuat matriks translasi
img_transition = cv.warpAffine(image, transition_matrix, (w, h)) # Melakukan translasi menggunakan matriks translasi

# Menampilkan gambar
plt.imshow(cv.cvtColor(img_transition, cv.COLOR_BGR2RGB))
plt.title("Translation")
plt.show()
