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

---


###  Kurulum ve Çalıştırma Rehberi

Bu projeyi bilgisayarınızda sorunsuz bir şekilde çalıştırmak için aşağıdaki adımları sırasıyla izleyiniz.

#### Adım 1: Projeyi Bilgisayarınıza İndirin
1. Bu sayfanın sağ üst köşesinde bulunan yeşil **"Code"** butonuna tıklayın.
2. Açılan menüden **"Download ZIP"** seçeneğine tıklayarak projeyi bilgisayarınıza indirin.
3. İnen ZIP dosyasını klasöre çıkartın (Örneğin, masaüstüne çıkartabilirsiniz).

#### Adım 2: Projeyi VS Code (veya Terminal) Üzerinde Açın
1. Bilgisayarınızda **Visual Studio Code (VS Code)** uygulamasını açın.
2. Üst menüden **File > Open Folder...** (Dosya > Klasör Aç...) yolunu izleyerek az önce çıkardığınız proje klasörünü seçin.
3. Proje açıldıktan sonra, VS Code'un üst menüsünden **Terminal > New Terminal** (Yeni Terminal) seçeneğine tıklayarak alt kısımda bir terminal penceresi açın.

#### Adım 3: Gerekli Kütüphanelerin Yüklenmesi
Açtığınız terminal ekranına aşağıdaki komutu yazıp `Enter`'a basarak projenin çalışması için gereken Python kütüphanelerini kurun:

```bash
pip install -r requirements.txt
```

#### Adım 4: Uygulamayı Başlatma
Kütüphanelerin kurulumu tamamlandıktan sonra, terminale aşağıdaki komutu yazıp `Enter`'a basarak uygulamayı çalıştırın:



```bash
python main.py

```



> ⚠️ **Önemli Not (İlk Çalıştırma Beklemesi):** Programı ilk kez başlattığınızda, yapay zeka analizleri için gerekli olan `all-MiniLM-L6-v2` dil modeli arka planda bir kereye mahsus internetten indirilecektir (Yaklaşık 90 MB). Bu nedenle **ilk açılışta kısa bir bekleme süresi olacaktır.** Model bilgisayarınıza kaydedildikten sonraki kullanımlarda sistem tamamen internetsiz (çevrimdışı) ve anında açılacaktır.



###  Nasıl Kullanılır?
1. Program açıldığında **"PDF Dosyası Yükle"** butonuna tıklayarak analiz edilecek CV'leri (PDF) seçin.
2. Alt kısımdaki metin kutusuna, aranılan **İş İlanı Metnini** (İngilizce) girin veya yapıştırın.
3. **"Analiz Başlat"** butonuna tıklayın ve uygulamanın arka planda işlemi bitirmesini bekleyin.
4. Sonuçları detaylı yüzdelik oranlar ve eksik beceriler tablosu halinde **"Sonuçlar"** sekmesinden inceleyebilirsiniz.

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
