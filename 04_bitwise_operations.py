"""
04 - Bitwise Operations (Bit Düzeyinde İşlemler)

Bu dosya OpenCV'de bitwise (mantıksal) işlemlerin nasıl kullanıldığını gösterir.
Özellikle maskeleme (masking) işlemlerinde çok sık kullanılır.

İşlemler:
- AND, OR, XOR, NOT
- Maskeleme (belirli bir bölgeyi seçmek)
"""

import cv2
import numpy as np

# ====================== 1. Basit Bitwise Örnekleri ======================

# İki siyah canvas oluşturuyoruz
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

# img1 içine beyaz bir dikdörtgen çiziyoruz
cv2.rectangle(img1, (50, 50), (250, 250), 255, -1)

# img2 içine beyaz bir daire çiziyoruz
cv2.circle(img2, (150, 150), 100, 255, -1)

# Bitwise İşlemleri
and_img = cv2.bitwise_and(img1, img2)
or_img  = cv2.bitwise_or(img1, img2)
xor_img = cv2.bitwise_xor(img1, img2)
not_img = cv2.bitwise_not(img1)

# Sonuçları göster
cv2.imshow("Rectangle", img1)
cv2.imshow("Circle", img2)
cv2.imshow("AND (Kesişim)", and_img)
cv2.imshow("OR (Birleşim)", or_img)
cv2.imshow("XOR (Fark)", xor_img)
cv2.imshow("NOT (Tersi)", not_img)

# ====================== 2. Gerçek Maskeleme Örneği ======================

img = cv2.imread("resim.jpg")

# Maske oluştur (siyah bir görüntü, aynı boyutlarda)
mask = np.zeros(img.shape[:2], dtype="uint8")

# Maske içine beyaz bir daire çiz (bu daire içindeki alan korunacak)
cv2.circle(mask, (150, 150), 100, 255, -1)

# Maskeyi orijinal görüntüye uygula
masked_img = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original Image", img)
cv2.imshow("Mask", mask)
cv2.imshow("Masked Image (Sadece Daire İçi)", masked_img)

print("Bitwise işlemler tamamlandı.")
print("Bir tuşa basarak pencereleri kapatabilirsiniz...")

cv2.waitKey(0)
cv2.destroyAllWindows()