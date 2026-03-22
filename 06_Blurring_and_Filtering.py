"""
06 - Blurring and Filtering (Bulanıklaştırma ve Filtreleme İşlemleri)

Bu dosya, OpenCV'de görüntüdeki gürültüyü azaltmak ve yumuşatmak için kullanılan
bulanıklaştırma (blurring) tekniklerini gösterir.

Her filtrenin kendine özgü kullanım amacı vardır.
"""

import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread("resim.jpg")

# Orijinal görüntüyü göster
cv2.imshow("Original Image", img)

# ==================== 1. Average Blur (Basit Ortalama Bulanıklaştırma) ====================
# Her pikseli, komşularının ortalamasıyla değiştirir. Basit ama kenarları fazla yumuşatır.
average = cv2.blur(img, (5, 5))

# ==================== 2. Gaussian Blur ====================
# Komşulara Gaussian dağılımına göre ağırlık verir. Daha doğal ve yumuşak sonuç verir.
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# ==================== 3. Median Blur ====================
# Komşuların ortanca (median) değerini alır.
# Özellikle "tuz-biber" (salt-and-pepper) gürültüsü için çok etkilidir.
median = cv2.medianBlur(img, 5)

# ==================== 4. Bilateral Filter ====================
# Hem uzamsal yakınlığı hem de renk benzerliğini dikkate alır.
# Gürültüyü azaltırken kenarları korur. Portre fotoğraflarında ve detay korumak istediğimizde tercih edilir.
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# ==================== Sonuçları Gösterme ====================
cv2.imshow("Average Blur", average)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Filter", bilateral)

print("Bulanıklaştırma işlemleri tamamlandı.")
print("\nKısa Özet:")
print("- Average Blur  : Basit ve hızlı, kenarları fazla yumuşatır")
print("- Gaussian Blur : Daha doğal görünüm sağlar")
print("- Median Blur   : Tuz-biber gürültüsü için en etkili yöntem")
print("- Bilateral     : Kenarları korurken gürültü azaltır (en gelişmiş)")

print("\nBir tuşa basarak pencereleri kapatabilirsiniz...")
cv2.waitKey(0)
cv2.destroyAllWindows()