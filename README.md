# Cv Uygunluk Karar Destek Sistemi

Bu projenin temel amacı, iş arayan adaylar ile işverenlerin beklentileri arasındaki dijital boşluğu veriye dayalı bir yöntemle doldurmaktır. Sadece bir dosya okuma aracı değil; bir mühendis adayının veya profesyonelin, hedeflediği pozisyona ne kadar yakın olduğunu gösteren dijital bir rehber geliştirmeyi hedefliyoruz.

## Projenin Amacı ve Kapsamı
* **Analiz:** PDF formatındaki özgeçmişlerin içeriği analiz edilerek, belirli bir iş tanımıyla olan anlamsal örtüşme düzeyi incelenir. 
* **Raporlama:** Kullanıcıya kişiselleştirilmiş bir uyumluluk raporu sunulacaktır. 
* **Verimlilik:** İşveren tarafında, yüzlerce başvuru arasından pozisyona teknik olarak en yakın profillerin hızlıca belirlenmesini sağlayarak zaman kaybını ve öznel hataları minimize etmeyi hedefler. 

## Teknik Yaklaşım
Sistemin temel çalışma prensibi, ham metin verilerini bilgisayarın işleyebileceği matematiksel modellere dönüştürmek üzerine kuruludur. Süreç şu dört ana aşamadan oluşacaktır: 

1. **Veri Edinme:** Python tabanlı **PyPDF2** kütüphanesi kullanılarak özgeçmişler dijital metne dönüştürülür. 
2. **Metin Ön İşleme (NLP):** **NLTK** kütüphanesi ile noktalama işaretleri ve anlam taşımayan bağlaçlar temizlenerek veri standart hale getirilir. 
3. **Vektörleştirme:** **Scikit-learn** kütüphanesindeki **TF-IDF** yöntemiyle metinler sayısal vektörlere dönüştürülür. 
4. **Benzerlik Ölçümü:** Vektörler arasındaki anlamsal yakınlık **Kosinüs Benzerliği** algoritması kullanılarak hesaplanır. 

