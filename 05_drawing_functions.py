"""
05 - Drawing Functions (Çizim Fonksiyonları)

Bu dosya OpenCV ile görüntünün üzerine şekil çizme, yazı yazma gibi işlemleri gösterir.
Çizim fonksiyonları özellikle nesne işaretleme, bounding box çizme ve görselleştirme için çok kullanılır.
"""

import cv2
import numpy as np

# Boş bir canvas (siyah görüntü) oluşturalım
img = np.zeros((500, 800, 3), dtype="uint8")

# ==================== Çizim Fonksiyonları ====================

# 1. Dikdörtgen çizme
# cv2.rectangle(img, sol_üst_nokta, sağ_alt_nokta, renk, kalınlık)
cv2.rectangle(img, (50, 50), (300, 250), (0, 255, 0), 3)        # Yeşil çerçeve
cv2.rectangle(img, (350, 100), (600, 300), (0, 0, 255), -1)     # Kırmızı dolu dikdörtgen (-1 = dolu)

# 2. Daire çizme
# cv2.circle(img, merkez, yarıçap, renk, kalınlık)
cv2.circle(img, (650, 150), 80, (255, 255, 0), 4)               # Sarı çerçeve daire
cv2.circle(img, (200, 400), 60, (255, 0, 255), -1)              # Mor dolu daire

# 3. Çizgi çizme
# cv2.line(img, başlangıç_noktası, bitiş_noktası, renk, kalınlık)
cv2.line(img, (0, 0), (800, 500), (255, 255, 255), 2)           # Beyaz diagonal çizgi

# 4. Yazı yazma (Text)
# cv2.putText(img, yazı, konum, font, font_boyutu, renk, kalınlık)
cv2.putText(img, "OpenCV Drawing", (50, 450), cv2.FONT_HERSHEY_SIMPLEX,
            1.2, (255, 255, 255), 3)

# ==================== Görüntüyü Gösterme ====================
cv2.imshow("Drawing Functions", img)

print("Çizim fonksiyonları tamamlandı.")
print("Bir tuşa basarak pencereyi kapatabilirsiniz...")

cv2.waitKey(0)
cv2.destroyAllWindows()