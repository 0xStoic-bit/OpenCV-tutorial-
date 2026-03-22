"""
07 - Thresholding and Edge Detection (Eşikleme ve Kenar Algılama)

Bu dosya, OpenCV'de görüntüyü siyah-beyaz hale getirme (threshold) ve
kenarları bulma (Canny Edge Detection) işlemlerini gösterir.
"""

import cv2
import numpy as np


#Görüntüyü yükle
img =cv2.imread("resim.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Original",img)
cv2.imshow("gray",gray)

# ==================== 1. Thresholding (Eşikleme) ====================

# Basit Binary Threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# 127'den büyük olan pikseller 255 (beyaz), küçük olanlar 0 (siyah) olur

# Otsu Threshold (Otomatik eşik değeri bulur - çok kullanışlı)
_, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ==================== 2. Edge Detection (Kenar Algılama) ====================

# Canny Edge Detection - En popüler kenar bulma algoritması
# 100 ve 200 = alt ve üst eşik değerleri
edges = cv2.Canny(gray, 100, 200)


# ==================== Sonuçları Gösterme ====================

cv2.imshow("Binary Threshold", binary)
cv2.imshow("Otsu Threshold", otsu)
cv2.imshow("Canny Edges", edges)

print("Threshold ve Edge Detection işlemleri tamamlandı.")
print("\nKısa Özet:")
print("- Binary Threshold : Sabit bir eşik değeriyle siyah-beyaz yapar")
print("- Otsu Threshold   : Otomatik en iyi eşik değerini bulur")
print("- Canny Edges      : Görüntüdeki kenarları tespit eder (en etkili yöntem)")

print("\nBir tuşa basarak pencereleri kapatabilirsiniz...")
cv2.waitKey(0)
cv2.destroyAllWindows()