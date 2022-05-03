# Hareket Algılama
## Uygulamanın Amacı
Bilgisayarda açık olan uygulamada (uygulama pencere ismi ile seçilecek) hareket eden nesneleri anlık olarak algılayan ve koordinatlarını bularak (ekranın sol üst köşesi 0,0 kabul edilecek) **pyautogui** kütüphanesi ile hareket eden bu nesneye tıklamak.

### Yapılanlar:
* Bilgisayarda çalışan uygulamayı pencere adını girerek yakalamak.
* Seçilen bu uygulamayı anlık olarak takip etmek.
* Son iki frame için **OpenCV** kütüphanesinde **absdiff** fonksiyonu kullanılarak yalnızca hareket eden nesneleri görmek.

[Normal Gif](https://media1.tenor.com/images/3d71dba30ffd29af9da30b88246fce34/tenor.gif)
[Absdiff Gif](https://media.tenor.com/images/c32747d599d34ab99341915ae4c66926/tenor.gif)
*Videos klasörünün içine iki durumu da video olarak ekledim.*

### Yapılacaklar:
* Absdiff fonksiyonuyla elde edilen çıktıda siyah olmayan (hareket olan) kısımların tespiti.
* Bu kısımların ekran üzerindeki koordinatlarının tespiti.
