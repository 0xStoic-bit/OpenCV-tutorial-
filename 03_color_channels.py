"""
03 - Color Channels (Renk Kanalları - Split & Merge)

Bu dosya, OpenCV'de renkli bir görüntünün nasıl üç ayrı kanala (Blue, Green, Red) ayrıldığını
ve tekrar birleştirildiğini gösterir.

Ayrıca sadece belirli bir renk kanalını görüntülemek için nasıl maske kullanıldığını da içerir.
"""

import cv2
import numpy as np

# Görüntüyü renkli olarak yükle
img = cv2.imread("resim.jpg")

# ==================== Renk Kanallarını Ayırma (Split) ====================
# cv2.split() fonksiyonu BGR görüntüyü 3 ayrı kanala ayırır
# OpenCV'de renk sırası RGB değil, BGR'dir!
b, g, r = cv2.split(img)

# Her kanal aslında tek renkli (gri tonlu) bir görüntüdür
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

# ==================== Kanalları Tekrar Birleştirme (Merge) ====================
# cv2.merge() ile kanalları tekrar birleştiriyoruz
img_merged = cv2.merge([b, g, r])

cv2.imshow("Merged Image (Original)", img_merged)

# ==================== Sadece Belirli Bir Renk Kanalını Gösterme ====================
# Boş (siyah) bir katman oluşturuyoruz (aynı boyutlarda)
zero = np.zeros(img.shape[:2], dtype="uint8")

# Sadece Kırmızı kanalı aktif olsun
only_red = cv2.merge([zero, zero, r])

# Sadece Yeşil kanalı aktif olsun
only_green = cv2.merge([zero, g, zero])

# Sadece Mavi kanalı aktif olsun
only_blue = cv2.merge([b, zero, zero])

cv2.imshow("Only Red", only_red)
cv2.imshow("Only Green", only_green)
cv2.imshow("Only Blue", only_blue)

print("Bir tuşa basarak tüm pencereleri kapatabilirsiniz...")
cv2.waitKey(0)
cv2.destroyAllWindows()