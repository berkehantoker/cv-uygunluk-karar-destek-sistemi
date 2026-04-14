import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Örnek veriler (İleride PyPDF2 ile dosyadan okunacaktır)
cv_metni = "Python, SQL, C# ve veri analizi konusunda deneyimli yazılım geliştirici."
is_ilani = "Python ve SQL bilen, veri odaklı projelerde çalışacak geliştirici aranıyor."

# Metinleri sayısal vektörlere dönüştürme (TF-IDF)
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([cv_metni, is_ilani])

# Kosinüs Benzerliği ile uyum skorunu hesaplama
score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

print(f"Cv Uygunluk Skoru: %{score * 100:.2f}")
