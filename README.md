Cv Uygunluk Karar Destek Sistemi

Bu proje, iş arayan adaylar ile işverenlerin beklentileri arasındaki dijital boşluğu veriye dayalı bir yöntemle doldurmayı amaçlamaktadır. Sistem, özgeçmişleri sadece bir dosya olarak okumakla kalmayıp, adayın hedeflediği pozisyona ne kadar yakın olduğunu gösteren dijital bir rehber görevi görür.

Projenin Amacı ve Kapsamı
Proje, PDF formatındaki özgeçmişlerin içeriğini analiz ederek belirli bir iş tanımıyla olan anlamsal örtüşme düzeyini inceler.

Kullanıcılara kişiselleştirilmiş bir uyumluluk raporu sunulmasını sağlar.

Adayların geri bildirim eksikliğini gidermeyi ve işverenlerin aday belirleme süreçlerindeki zaman kaybını minimize etmeyi hedefler.

Teknik Yaklaşım
Sistem, ham metin verilerini matematiksel modellere dönüştürerek şu aşamalarla çalışır:

Veri Edinme ve Metin Ayıklama: Python tabanlı PyPDF2 kütüphanesi ile PDF içerikleri dijital metne dönüştürülür.

Metin Ön İşleme (NLP): NLTK kütüphanesi kullanılarak noktalama işaretleri ve anlam taşımayan bağlaçlar (ve, ile, de vb.) temizlenir, veriler standart hale getirilir.

Vektörleştirme ve Benzerlik Ölçümü: Scikit-learn kütüphanesindeki TF-IDF yöntemiyle metinler sayısal vektörlere dönüştürülür. Ardından Kosinüs Benzerliği (Cosine Similarity) algoritması ile %0-100 arası uyumluluk skoru hesaplanır.

Eksik Yetenek Analizi: Pandas kütüphanesi yardımıyla iş ilanındaki kritik anahtar kelimeler ile özgeçmiş karşılaştırılarak eksik beceriler raporlanır.
