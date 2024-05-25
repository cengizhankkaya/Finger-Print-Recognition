# SIFT Kullanarak Parmak İzi Eşleştirme

### Bu proje, OpenCV'de Ölçekten Bağımsız Öznitelik Dönüşümü (SIFT) algoritması ve FLANN tabanlı eşleştirici kullanarak değiştirilmiş bir parmak izini gerçek bir parmak iziyle eşleştirme yöntemini göstermektedir.
## Proje Yapısı
```js
}
  ├── SOCOFing
  │   ├── Altered
  │   │   └── Altered-Easy
  │   │       └── 1__M_Left_index_finger_CR.BMP
  │   └── Real
  │       ├── 1__M_Left_index_finger.BMP
  │       ├── 2__M_Left_index_finger.BMP
  │       ├── ...
  ├── main.py
  └── README.md
}
```

## Gereksinimler
### Bu projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

<ol>
    <li>OpenCV</li>
    <li>NumPy</li>
</ol>

### Bu kütüphaneleri pip kullanarak yükleyebilirsiniz:
```js
 pip install opencv-python-headless numpy
```
## Nasıl Çalışır
### Script, değiştirilmiş bir parmak izi görüntüsünü işler ve bir dizi gerçek parmak izi görüntüsünden en iyi eşleşmeyi bulmaya çalışır. SIFT algoritması, anahtar noktaları tespit etmek ve tanımlayıcıları hesaplamak için kullanılır. Bu tanımlayıcılar, FLANN tabanlı eşleştirici kullanılarak eşleştirilir. En iyi eşleşme, iyi eşleşmelerin anahtar nokta sayısına oranına göre belirlenir.
## Detaylı Adımlar

<ul>
	<li>Değiştirilmiş Parmak İzini Yükle: OpenCV kullanarak değiştirilmiş parmak izi görüntüsünü yükleyin.</li>
</ul>
<ul>
	<li>SIFT'i Başlat: Anahtar noktaları tespit etmek ve tanımlayıcıları hesaplamak için bir SIFT nesnesi oluşturun.</li>
</ul>
<ul>
	<li>Gerçek Parmak İzi Görsellerini Dolaş: Her gerçek parmak izi görüntüsü için:
     <ul> - Görüntüyü yükleyin. </ul>
     <ul> - Hem değiştirilmiş hem de gerçek parmak izi görüntüleri için anahtar noktaları tespit edin ve tanımlayıcıları hesaplayın. </ul>
     <ul> - Tanımlayıcılar arasındaki eşleşmeleri bulmak için FLANN tabanlı eşleştirici kullanın. </ul>
     <ul> - Mesafe kriterine göre iyi eşleşmeleri filtreleyin. </ul>
     <ul> - İyi eşleşmelerin toplam anahtar nokta sayısına oranına göre eşleşme skorunu hesaplayın. </ul>
     <ul> - Eğer mevcut eşleşme skoru önceki en iyi skordan yüksekse, en iyi eşleşmeyi güncelleyin. </ul>
     <ul> - En İyi Eşleşmeyi Göster: Değiştirilmiş parmak izi ile en iyi eşleşen gerçek parmak izi arasındaki eşleşmeleri çizin ve sonucu gösterin. </ul>
  </li>
</ul>
<ul>
	<li>En İyi Eşleşmeyi Göster: Değiştirilmiş parmak izi ile en iyi eşleşen gerçek parmak izi arasındaki eşleşmeleri çizin ve sonucu gösterin.</li>
</ul>

## Scripti Çalıştırma
### Scripti çalıştırmak için şu komutu kullanın:
```js
 python main.py
```
### Script, her parmak izi işlenirken ilerlemeyi yazdıracak ve en iyi eşleşen parmak izi ile eşleşme skorunu gösterecektir.
## Örnek Çıktı
```js

0
1__M_Left_index_finger.BMP
10
11__M_Left_index_finger.BMP
20
21__M_Left_index_finger.BMP
...
BEST MATCH: 42__M_Left_index_finger.BMP
SCORE: 85.71428571428571


```
### Bir pencere açılacak ve solda değiştirilmiş parmak izi, sağda en iyi eşleşen gerçek parmak izi gösterilecek, ve eşleşen anahtar noktalar arasındaki çizgilerle birlikte.
![Ekran görüntüsü 2024-05-08 204316](https://github.com/cengizhankkaya/Finger-Print-Recognition/assets/92298156/9dec9021-bc75-4d33-8f13-e34bac3b586e)

# Notlar
<ul>
	<li>Daha iyi sonuçlar için eşleşme filtreleme adımındaki mesafe eşiğini veri setinize göre ayarlayın.</li>
  <li>Değiştirilmiş ve gerçek parmak izi görüntülerinin yollarının doğru şekilde belirtilmiş olduğundan emin olun.</li>
</ul>

## Bu proje, SIFT özelliklerini kullanarak parmak izi eşleştirme için basit ancak etkili bir yaklaşımı göstermektedir. Performans ve doğruluğu artırmak için belirli gereksinimlere ve veri setlerine göre ayarlamalar yapılabilir.


