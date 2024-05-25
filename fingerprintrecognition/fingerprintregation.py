import os
import cv2

# Altered (değiştirilmiş) parmak izi örneğini yükle
sample = cv2.imread("SOCOFing/Altered/Altered-Easy/1__M_Left_index_finger_CR.BMP") 

# En iyi eşleşme skoru ve eşleşen dosya adını tutmak için değişkenler
best_score = 0
filename = None
image = None 
kp1, kp2, mp = None, None, None

# SIFT nesnesi oluşturma
sift = cv2.SIFT_create()
counter = 0

# Real (gerçek) parmak izi görüntülerini içeren klasördeki her dosya için döngü
for file in [file for file in os.listdir("SOCOFing/Real")]:
    if counter % 10 == 0:
        print(counter)
        print(file)
    counter += 1
    
    # Gerçek parmak izi görüntüsünü yükle
    fingerprint_image = cv2.imread("SOCOFing/Real/" + file)

    # Örnek ve gerçek parmak izi görüntüsü için SIFT anahtar noktaları ve tanımlayıcıları bulma
    keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

    # FLANN tabanlı eşleştirici kullanarak eşleşmeleri bulma
    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {}).knnMatch(descriptors_1, descriptors_2, k=2)
    match_points = []

    # İyi eşleşmeleri filtreleme
    for p, q in matches:
        if p.distance < 0.1 * q.distance:
            match_points.append(p)

    # Anahtar noktaların sayısını belirleme
    keypoints = min(len(keypoints_1), len(keypoints_2))

    # Eşleşen nokta oranını hesaplama ve en iyi skoru güncelleme
    if len(match_points) / keypoints * 100 > best_score:
       best_score = len(match_points) / keypoints * 100 
       filename = file
       image = fingerprint_image
       kp1, kp2, mp = keypoints_1, keypoints_2, match_points

# En iyi eşleşme dosyasını ve skorunu yazdırma
print("BEST MATCH: " + filename)
print("SCORE: " + str(best_score))

# Eşleşmeleri içeren sonucu çizme ve gösterme
result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
result = cv2.resize(result, None, fx=4, fy=4)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
