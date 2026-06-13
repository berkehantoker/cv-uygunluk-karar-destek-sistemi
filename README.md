# CV Uygunluk Karar Destek Sistemi

Bu proje, Python ile geliştirilmiş arayüzlü bir **CV - İş İlanı Uyum Analiz Sistemi**dir. Sistem, PDF formatındaki bir CV dosyasını okuyarak kullanıcının girdiği iş ilanı metniyle karşılaştırır ve kullanıcıya üç farklı analiz sonucu sunar:

1. **TF-IDF Skoru**
2. **BERT Skoru**
3. **Nihai Skor**

Proje, Bursa Uludağ Üniversitesi Mühendislik Fakültesi Bilgisayar Mühendisliği Bölümü **Python Programlamaya Giriş** dersi kapsamında hazırlanmıştır.

---

## Proje Amacı

İnsan kaynakları süreçlerinde çok sayıda CV’nin tek tek incelenmesi zaman kaybına ve değerlendirme hatalarına yol açabilir. Bu proje, adayın CV’si ile iş ilanı arasındaki uyumu daha hızlı, nesnel ve açıklanabilir şekilde değerlendirmeyi amaçlayan bir karar destek sistemi sunar.

Sistem, PDF formatındaki CV dosyasından metin çıkarır, iş ilanı metniyle karşılaştırır ve sonuçları modern bir masaüstü arayüzü üzerinden kullanıcıya gösterir.

---


## Kullanılan Teknolojiler ve Tercih Nedenleri
* **Python:** Tüm sistemin temel programlama dili olarak esnekliği ve geniş kütüphane desteği nedeniyle tercih edilmiştir.
* **Sentence-Transformers (BERT - `all-MiniLM-L6-v2`):** Sistemin ana beynidir. Sadece kelime saymak yerine "Software Developer" ile "Python Programmer" kavramlarının uzayda birbirine yakın olduğunu bilmesi ve anlamsal eşleşme yapabilmesi için entegre edilmiştir. Hafif ve çevrimdışı çalışabilen bir model olduğu için seçilmiştir.
* **Scikit-learn (TF-IDF):** BERT modelinin bazen kaçırabileceği spesifik teknik terimleri (C#, .NET, React vb.) nokta atışı yakalamak ve sistemi hibrit (kelime + anlam) bir yapıya dönüştürmek için teknik danışman olarak kullanılmıştır.
* **PyQt5 & QThread:** Kullanıcı arayüzünü (UI) modern ve karanlık temalı (Dark Mode) tasarlamak için kullanılmıştır. Ağır yapay zeka hesaplamalarının arayüzü dondurmasını engellemek amacıyla `worker.py` içinde asenkron iş parçacığı (QThread) mimarisi kurgulanmıştır.
* **PDFPlumber & Pandas:** PDF'lerin içindeki görünmez karakterleri ve tabloları en stabil şekilde okuyabilmek için PDFPlumber; analiz sonuçlarını temiz bir şekilde Excel'e aktarabilmek için Pandas kullanılmıştır.

---

## Proje Dosya Yapısı

cv-uygunluk-karar-destek-sistemi/

- main.py
- utils.py
- worker.py
- requirements.txt
- README.md
- .gitignore



## Kurulum

Projeyi bilgisayarınıza indirdikten sonra proje klasöründe terminal açın.

Gerekli kütüphaneleri yüklemek için:

    pip install -r requirements.txt

---

## requirements.txt

Projenin çalışması için gerekli kütüphaneler:

PyQt5
pdfplumber
scikit-learn
sentence-transformers
pandas
openpyxl
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
