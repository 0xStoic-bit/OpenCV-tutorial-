"""
08 - Contours (Konturlar / Sınırlar)

Bu dosya, OpenCV'de bir görüntüdeki nesnelerin sınırlarını (kontur) nasıl bulacağımızı gösterir.
Kontur bulma, nesne tespiti, şekil analizi ve sayma işlemleri için çok önemlidir.
"""

import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread("resim.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold (eşikleme) uyguluyoruz
# 127 eşik değeri: 127'den büyük pikseller beyaz (255), küçük olanlar siyah (0) olur
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# ==================== Kontur Bulma ====================
# cv2.findContours() → Görüntüdeki beyaz bölgelerin sınırlarını bulur
# RETR_EXTERNAL   → Sadece dış konturları alır (iç içe olanları ignore eder)
# CHAIN_APPROX_SIMPLE → Kontur noktalarını sıkıştırarak daha az bellek kullanır
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Toplam bulunan kontur sayısı: {len(contours)}")

# ==================== Konturları Çizme ====================
# cv2.drawContours() → Bulunan konturları orijinal görüntü üzerine çizer
# -1 → Tüm konturları çiz
# (0, 255, 0) → Yeşil renk
# 3 → Çizgi kalınlığı
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# ==================== Sonuçları Gösterme ====================
cv2.imshow("Threshold Image", thresh)
cv2.imshow("Contours Detected", img)

print("\nAçıklama:")
print("- Threshold ile görüntüyü siyah-beyaz hale getirdik")
print("- findContours ile nesnelerin sınırlarını bulduk")
print("- drawContours ile bu sınırları yeşil renkle işaretledik")

cv2.waitKey(0)
cv2.destroyAllWindows()