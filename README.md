# Cv Uygunluk Karar Destek Sistemi

Bu projenin temel amacı, iş arayan adaylar ile işverenlerin beklentileri arasındaki dijital boşluğu veriye dayalı bir yöntemle doldurmaktır. Sadece bir dosya okuma aracı değil; bir mühendis adayının veya profesyonelin, hedeflediği pozisyona ne kadar yakın olduğunu gösteren dijital bir rehber geliştirmeyi hedefliyoruz.

## Projenin Amacı ve Kapsamı
* [cite_start]**Analiz:** PDF formatındaki özgeçmişlerin içeriği analiz edilerek, belirli bir iş tanımıyla olan anlamsal örtüşme düzeyi incelenir. [cite: 19]
* [cite_start]**Raporlama:** Kullanıcıya kişiselleştirilmiş bir uyumluluk raporu sunulacaktır. [cite: 19]
* [cite_start]**Verimlilik:** İşveren tarafında, yüzlerce başvuru arasından pozisyona teknik olarak en yakın profillerin hızlıca belirlenmesini sağlayarak zaman kaybını ve öznel hataları minimize etmeyi hedefler. [cite: 32]

## Teknik Yaklaşım
Sistemin temel çalışma prensibi, ham metin verilerini bilgisayarın işleyebileceği matematiksel modellere dönüştürmek üzerine kuruludur. [cite_start]Süreç şu dört ana aşamadan oluşacaktır: [cite: 21]

1. [cite_start]**Veri Edinme:** Python tabanlı **PyPDF2** kütüphanesi kullanılarak özgeçmişler dijital metne dönüştürülür. [cite: 22]
2. [cite_start]**Metin Ön İşleme (NLP):** **NLTK** kütüphanesi ile noktalama işaretleri ve anlam taşımayan bağlaçlar temizlenerek veri standart hale getirilir. [cite: 24]
3. [cite_start]**Vektörleştirme:** **Scikit-learn** kütüphanesindeki **TF-IDF** yöntemiyle metinler sayısal vektörlere dönüştürülür. [cite: 26]
4. [cite_start]**Benzerlik Ölçümü:** Vektörler arasındaki anlamsal yakınlık **Kosinüs Benzerliği** algoritması kullanılarak hesaplanır. [cite: 27]

