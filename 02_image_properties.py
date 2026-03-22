"""
02-Image Properties (Görüntü Özellikleri)

Bu dosya, bir görüntünün temel özelliklerini nasıl öğrenebileceğimizi gösterir.
Özellikle shape, dtype ve size kavramları OpenCV öğrenirken çok önemlidir.
"""

import cv2
import numpy as np

#Görüntüyü renkli olarak yükle
img = cv2.imread("resim.jpg",0)

# ==================== Görüntü Özellikleri ====================

print("Görüntü Boyutları(shape) :",img.shape)
print(" -Yükseklik (Height) : ",img.shape[0])
print(" -Genişlik (Width)   : ",img.shape[1])
print(" -Kanal Sayısı       :",img.shape[2])

print("\nVeri Tipi(dytpe)   :",img.dtype)
# uint8 = 0-255 arası değerler. OpenCV görüntüleri genellikle bu tipte saklanır.


print("\nToplam Piksel Sayısı (size) :", img.size)
print("(Yükseklik x Genişlik x Kanal) =", img.shape[0] * img.shape[1] * img.shape[2])



# ==================== Görüntüyü Gösterme ====================
cv2.imshow("Orijinal Görüntü", img)

print("\nBir tuşa basarak pencereyi kapatabilirsiniz...")
cv2.waitKey(0)
cv2.destroyAllWindows()