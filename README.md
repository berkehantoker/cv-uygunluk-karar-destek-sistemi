# CV Uygunluk Karar Destek Sistemi

Bu proje, Python ile geliştirilmiş arayüzlü bir **CV - İş İlanı Uyum Analiz Sistemi**dir. Sistem, PDF formatındaki bir CV dosyasını okuyarak kullanıcının girdiği iş ilanı metniyle karşılaştırır ve kullanıcıya iki farklı analiz sonucu sunar:

1. **Metin Benzerliği Skoru**
2. **Beceri Uyumu Skoru**

Proje, Bursa Uludağ Üniversitesi Mühendislik Fakültesi Bilgisayar Mühendisliği Bölümü **Python Programlamaya Giriş** dersi kapsamında hazırlanmıştır.

---

## Proje Amacı

İnsan kaynakları süreçlerinde çok sayıda CV’nin tek tek incelenmesi zaman kaybına ve değerlendirme hatalarına yol açabilir. Bu proje, adayın CV’si ile iş ilanı arasındaki uyumu daha hızlı, nesnel ve açıklanabilir şekilde değerlendirmeyi amaçlayan bir karar destek sistemi sunar.

Sistem, PDF formatındaki CV dosyasından metin çıkarır, iş ilanı metniyle karşılaştırır ve sonuçları modern bir masaüstü arayüzü üzerinden kullanıcıya gösterir.

---

## Temel Özellikler

- PDF formatındaki CV dosyasından metin çıkarma
- İş ilanı metnini kullanıcıdan alma
- NLTK ile metin ön işleme
- TF-IDF ve Cosine Similarity ile metin benzerliği hesaplama
- Teknik beceri sözlüğü ile beceri eşleştirme
- Eksik becerileri tablo halinde gösterme
- PyQt5 ile modern karanlık temalı masaüstü arayüzü
- Analizi arka planda çalıştırarak arayüzün donmasını engelleme

---

## Kullanılan Teknolojiler

| Teknoloji / Kütüphane | Kullanım Amacı |
|---|---|
| Python | Ana programlama dili |
| PyQt5 | Grafiksel kullanıcı arayüzü |
| PyPDF2 | PDF dosyasından metin çıkarma |
| NLTK | Stop-word temizliği ve metin ön işleme |
| scikit-learn | TF-IDF ve Cosine Similarity hesaplama |
| pandas | Eksik becerilerin tablo halinde raporlanması |
| re | Regex tabanlı metin temizleme ve beceri eşleştirme |
| QThread | Analizi arka planda çalıştırma |

---

## Proje Dosya Yapısı

cv-uygunluk-karar-destek-sistemi/

- main.py
- utils.py
- worker.py
- requirements.txt
- README.md
- .gitignore


---

## Dosyaların Görevleri

**main.py:** PyQt5 arayüzünü içerir. CV yükleme, iş ilanı girme ve sonuçları gösterme işlemleri burada yapılır.

**utils.py:** PDF okuma, metin temizleme, TF-IDF hesaplama ve beceri eşleştirme fonksiyonlarını içerir.

**worker.py:** Analizin arayüzü dondurmadan arka planda çalışmasını sağlar.

---

## Kurulum

Projeyi bilgisayarınıza indirdikten sonra proje klasöründe terminal açın.

Gerekli kütüphaneleri yüklemek için:

    pip install -r requirements.txt

---

## requirements.txt

Projenin çalışması için gerekli kütüphaneler:

- PyQt5
- PyPDF2
- pandas
- nltk
- scikit-learn

---

## Çalıştırma

Programı çalıştırmak için:

    python main.py

Program açıldıktan sonra:

1. PDF dosyasını yükleyin.
2. İş ilanı metnini ilgili alana yazın veya yapıştırın.
3. Analiz Başlat butonuna tıklayın.
4. Sonuçları Sonuçlar sekmesinden görüntüleyin.

---

## Skorlar

**Metin Benzerliği Skoru:** CV ve iş ilanı metinlerinin TF-IDF ve Cosine Similarity ile hesaplanan genel benzerlik skorudur.

**Beceri Uyumu Skoru:** İş ilanında istenen teknik becerilerin kaç tanesinin CV’de bulunduğunu gösterir.

---

## Veritabanı Bilgisi

Bu projede herhangi bir veritabanı kullanılmamıştır.

---

## Veri Seti Bilgisi

Bu projede harici bir veri seti kullanılmamıştır. Testler örnek CV dosyaları ve örnek iş ilanı metinleri üzerinden gerçekleştirilmiştir.

---

## Grup Üyeleri

- Abdullah Seydi
- Osman Berkehan Toker
- Alihan Yalçın
