# CV Uygunluk Karar Destek Sistemi

Bu proje, Python ile geliştirilmiş arayüzlü bir **CV - İş İlanı Uyum Analiz Sistemi**dir. Sistem, PDF formatındaki bir CV dosyasını okuyarak kullanıcının girdiği iş ilanı metniyle karşılaştırır ve kullanıcıya iki farklı analiz sonucu sunar:

1. **Metin Benzerliği Skoru**
2. **Beceri Uyumu Skoru**

Proje, Bursa Uludağ Üniversitesi Mühendislik Fakültesi Bilgisayar Mühendisliği Bölümü **Pythonla Programlamaya Giriş** dersi kapsamında hazırlanmıştır.

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

## Proje Mimarisi

Proje üç ana Python dosyasından oluşur:

```text
cv-uygunluk-karar-destek-sistemi/
│
├── main.py
├── utils.py
├── worker.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── docs/
│   └── Proje_Raporu_CV_Uygunluk_Karar_Destek_Sistemi.pdf
│
└── screenshots/
    └── arayuz.png
Dosyaların Görevleri
main.py

main.py, uygulamanın grafiksel kullanıcı arayüzünü içerir.

Bu dosyada kullanıcı:

PDF formatındaki CV dosyasını yükler.
İş ilanı metnini girer.
Analizi başlatır.
Sonuçları sekmeli arayüz üzerinden görüntüler.

Arayüzde iki ana sekme bulunur:

Giriş (Input): CV yükleme ve iş ilanı metni girme alanı
Sonuçlar: Skorların ve beceri tablolarının gösterildiği alan
utils.py

utils.py, projenin çekirdek analiz fonksiyonlarını içerir.

Bu dosyada bulunan temel işlemler:

PDF dosyasından metin çıkarma
Teknik terim normalizasyonu
Metin temizleme
TF-IDF ile metinleri vektörleştirme
Cosine Similarity ile metin benzerliği hesaplama
Teknik beceri sözlüğü ile beceri eşleştirme

Sistemde C#, C++, .NET, ASP.NET gibi teknik ifadeler analiz sırasında bozulmaması için normalize edilir.

Örneğin:

C#      -> csharp
C++     -> cplusplus
.NET    -> dotnet
ASP.NET -> aspnet
worker.py

worker.py, analiz işleminin arka planda çalışmasını sağlar.

PyQt5 arayüzlerinde uzun süren işlemler doğrudan ana ekranda çalıştırılırsa program donabilir. Bu nedenle analiz işlemi QThread kullanılarak ayrı bir iş parçacığında çalıştırılır.

Bu yapı sayesinde:

Arayüz analiz sırasında donmaz.
Kullanıcıya işlem durumu gösterilir.
Analiz tamamlandığında sonuçlar arayüze aktarılır.
Sistem Nasıl Çalışır?

Sistem şu işlem hattını takip eder:

Kullanıcı PDF formatındaki CV dosyasını yükler.
Kullanıcı iş ilanı metnini arayüze girer.
PyPDF2 ile CV dosyasındaki metin çıkarılır.
CV ve iş ilanı metni küçük harfe çevrilir.
Noktalama işaretleri ve gereksiz kelimeler temizlenir.
C#, C++, .NET, ASP.NET gibi özel teknik terimler normalize edilir.
TF-IDF yöntemi ile CV ve iş ilanı sayısal vektörlere dönüştürülür.
Cosine Similarity ile genel metinsel benzerlik skoru hesaplanır.
Teknik beceri sözlüğü ile iş ilanındaki becerilerin CV’de olup olmadığı kontrol edilir.
Gerekli beceriler, CV’de bulunan beceriler ve eksik beceriler tablo halinde gösterilir.
Skorların Açıklaması

Sistem kullanıcıya iki farklı skor sunar.

1. Metin Benzerliği Skoru

Bu skor, CV metni ile iş ilanı metninin TF-IDF ve Cosine Similarity yöntemiyle hesaplanan genel metinsel benzerliğini gösterir.

Bu skor, iki metnin kelime ve ifade düzeyinde ne kadar benzer olduğunu ölçer. Ancak tek başına adayın işe uygunluğunu kesin olarak belirlemez.

Örneğin CV çok uzun, iş ilanı çok kısa olduğunda veya CV’de eğitim, tarih, kişisel bilgiler ve proje açıklamaları fazla olduğunda TF-IDF skoru düşük çıkabilir.

Bu nedenle bu skor sistemde yardımcı metrik olarak kullanılır.

2. Beceri Uyumu Skoru

Bu skor, iş ilanında istenen teknik becerilerin kaç tanesinin CV’de bulunduğunu gösterir.

Örneğin iş ilanında 10 teknik beceri isteniyor ve CV’de bunlardan 7 tanesi bulunuyorsa:

Beceri Uyumu = 7 / 10 * 100 = %70

Bu projede ana karar destek çıktısı beceri uyumu skorudur.

Teknik Beceri Sözlüğü

Sistem, açıklanabilir bir beceri analizi yapabilmek için önceden tanımlanmış bir teknik beceri sözlüğü kullanır.

Bu sözlük sayesinde iş ilanında geçen teknik beceriler tespit edilir ve CV içerisinde bulunup bulunmadığı kontrol edilir.

Örnek beceriler:

Python
Java
JavaScript
TypeScript
C#
C++
.NET
ASP.NET
MVC
Entity Framework
SQL
MySQL
PostgreSQL
MongoDB
Git
HTML
CSS
Bootstrap
React
Node.js
Machine Learning
Deep Learning
Natural Language Processing
Data Science
Pandas
NumPy
TensorFlow
PyTorch
AWS
Azure
Cloud
Docker
Kubernetes
REST API

Bu sözlük genişletilebilir yapıdadır. Farklı sektörlere veya farklı iş ilanlarına göre yeni teknik beceriler eklenebilir.

Kurulum

Öncelikle projeyi bilgisayarınıza klonlayın:

git clone https://github.com/kullanici-adiniz/cv-uygunluk-karar-destek-sistemi.git
cd cv-uygunluk-karar-destek-sistemi

Sanal ortam oluşturmanız önerilir:

python -m venv venv

Windows için sanal ortamı aktif edin:

venv\Scripts\activate

Gerekli kütüphaneleri yükleyin:

pip install -r requirements.txt
requirements.txt

Projenin çalışması için gerekli kütüphaneler:

PyQt5
PyPDF2
pandas
nltk
scikit-learn
Çalıştırma

Programı çalıştırmak için:

python main.py

Program açıldıktan sonra:

PDF Dosyasını Yükle butonuna tıklayın.
CV PDF dosyasını seçin.
İş ilanı metnini ilgili alana yazın veya yapıştırın.
Analiz Başlat butonuna tıklayın.
Sonuçları Sonuçlar sekmesinden görüntüleyin.
Örnek İş İlanı Metni

Aşağıdaki metni uygulamadaki iş ilanı alanında test amacıyla kullanabilirsiniz:

We are looking for a software developer with strong knowledge of Python, C#, ASP.NET, SQL, Git, Docker and Machine Learning. The candidate should have experience with MVC architecture, Entity Framework and database systems.
Örnek Çıktı

Program sonuç ekranında şu bilgiler gösterilir:

Metin Benzerliği
Beceri Uyumu
İş ilanında gereken beceriler
CV’de bulunan beceriler
Eksik beceriler

Örnek çıktı:

Metin Benzerliği: 13.25%
Beceri Uyumu: 77.78%

Gereken Beceriler:
- Python
- C#
- ASP.NET
- SQL
- Git
- Docker
- Machine Learning

CV'de Bulunan Beceriler:
- Python
- C#
- SQL
- Git

Eksik Beceriler:
- ASP.NET
- Docker
- Machine Learning
Uygulama Arayüzü

screenshots klasörüne uygulama ekran görüntüsü eklendiğinde aşağıdaki satır aktif olarak kullanılabilir:

![Uygulama Arayüzü](screenshots/arayuz.png)
Veritabanı Bilgisi

Bu projede herhangi bir veritabanı kullanılmamıştır.

Sistem, kullanıcının yüklediği PDF CV dosyasını ve arayüze girilen iş ilanı metnini anlık olarak analiz eder. Bu nedenle ayrıca veritabanı oluşturma veya veritabanı bağlantısı yapma adımı bulunmamaktadır.

Veri Seti Bilgisi

Bu projede harici bir veri seti kullanılmamıştır.

Testler, grup üyelerine ait örnek CV dosyaları ve örnek iş ilanı metinleri üzerinden gerçekleştirilmiştir. Kişisel veri güvenliği açısından gerçek CV dosyalarının repoya yüklenmemesi önerilir.

Sınırlılıklar

Bu proje bir karar destek prototipidir. Aşağıdaki sınırlılıklara sahiptir:

PyPDF2 bazı tasarımsal veya çok sütunlu PDF dosyalarında metni eksik okuyabilir.
TF-IDF skoru, CV’nin işe uygunluğunu tek başına tam olarak belirlemez.
Beceri analizi, önceden tanımlanmış teknik beceri sözlüğüne bağlıdır.
Sistem deneyim süresi veya tecrübe kalitesi gibi semantik detayları derinlemesine ayırt edemez.
Görsel tabanlı CV dosyalarında OCR desteği olmadığı için metin çıkarma başarısız olabilir.
Sistem mevcut haliyle İngilizce teknik CV ve İngilizce iş ilanı metinleri üzerinde daha sağlıklı çalışacak şekilde tasarlanmıştır.
Geliştirme Önerileri

İlerleyen sürümlerde proje şu özelliklerle geliştirilebilir:

OCR desteği eklenerek görsel tabanlı CV’lerin okunması
Teknik beceri sözlüğünün JSON dosyasından yönetilmesi
CSV veya Excel formatında rapor çıktısı alınması
BERT, Word2Vec veya Transformer tabanlı semantik modellerle daha gelişmiş analiz yapılması
Web tabanlı arayüz geliştirilmesi
İş ilanı metninin otomatik olarak web sayfasından alınması
Deneyim süresi ve beceri seviyesi gibi bilgilerin ayrıca analiz edilmesi
Grup Üyeleri
Abdullah Seydi
Osman Berkehan Toker
Alihan Yalçın
Ders Bilgisi
Üniversite: Bursa Uludağ Üniversitesi
Fakülte: Mühendislik Fakültesi
Bölüm: Bilgisayar Mühendisliği
Ders: Pythonla Programlamaya Giriş
Lisans

Bu proje eğitim amacıyla geliştirilmiştir.
