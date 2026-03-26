# Excel Satır Bükücü 

Bu script, Excel dosyasındaki tek bir hücre içinde satır satır bulunan metni aşağı doğru ayrı satırlara böler.

  ## Amacı ve Çalışma Mantığı

  Örnek olarak `A1` hücresinde şu veri varsa:
  
  Merhaba
  Nasılsın
  Bugün hava güzel
  
  Script bunu A sütununda şu şekilde yazar:
  
  - A1 -> Merhaba
  - A2 -> Nasılsın
  - A3 -> Bugün hava güzel
  
# Excel'den QR Kod Üretici

Bu proje, Excel dosyasındaki A sütununda bulunan metin, URL, sayı veya benzeri içerikleri okuyarak her satır için ayrı bir QR kod üretmek amacıyla hazırlanmıştır.

  ## Projenin Amacı

  Excel'de yer alan hücre içeriklerini hızlı şekilde QR koda dönüştürmek için kullanılır.

  Örneğin A sütununda şunlar olabilir:

  - Web adresi
  - Ürün kodu
  - Seri numarası
  - Metin
  - Sayı
  - Telefon numarası
  - Açıklama metni
  
  Bu script, her dolu hücre için bir QR kod görseli oluşturur.
    
  ## Ne Yapar?
    
  - Excel dosyasını okur
  - A sütunundaki verileri alır
  - Boş olmayan her hücre için QR kod üretir
  - QR görsellerini klasöre kaydeder
  - İstenirse çıktı Excel dosyasına ilgili QR dosya yolunu yazar
  
  ## Desteklenen Veri Türleri
  
  Bu proje aşağıdaki içerikler için uygundur:
  
  - Yazı
  - URL
  - Sayı
  - Karışık metin
  - Kod veya kısa açıklama
  
  ## Desteklenmeyen İçerikler
  
  Bu proje özellikle şu içerikler için tasarlanmamıştır:
  
  - Resim
  - Video
  - Ses dosyası
  - Medya dosyaları
  
  Yani hücrede yazı tabanlı ne varsa QR koda çevrilir, medya dosyaları işlenmez.
  
## Kur
  
```bash
pip install -r requirements.txt
