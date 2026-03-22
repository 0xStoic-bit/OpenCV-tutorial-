

"""
OpenCV Basics - Görüntü Okuma ve Gösterme
Bu dosya OpenCV'nin en temel fonksiyonlarını içeririr
"""

import numpy as np
import cv2

# ==================== Görüntü Okuma ====================
# cv2.imread() fonksiyonu 2 parametre alır:
# 1. parametre: resim yolu
# 2. parametre: okuma modu
# 1 = Renkli (BGR)
# 0 = Gri tonlamalı
# -1 = Orijinal (alfa kanalı varsa dahil)

img_color = cv2.imread("../resim.jpg", 1)
img_gray = cv2.imread("../resim.jpg", 0)

# ==================== Görüntü Gösterme ====================
cv2.imshow("Renkli Görüntü",img_color)
cv2.imshow("Gri Görüntü",img_gray)

# Pencereyi ekranın belirli bir konumuna taşıma işlemi
cv2.moveWindow("Renkli görüntü",0,0)

# ==================== Bekleme ve Kapatma ====================
print("Bir tuşa basarak pencereleri kapatabilirsiniz...")
cv2.waitKey(0)          # 0 = Herhangi bir tuşa basana kadar beklemesi için kullanılır ve içine aldığı integer değer milisaniye cinsindedir
cv2.destroyAllWindows() # Tüm pencereleri kapat

