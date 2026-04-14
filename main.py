import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cv_match(cv_text, job_desc):
    # Metinleri listeye al
    documents = [cv_text, job_desc]
    
    # Kelimeleri sayısallaştır (TF-IDF)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Kosinüs Benzerliğini hesapla (1. satır ile 2. satır karşılaştırması)
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    return similarity_matrix[0][0] * 100

# Örnek Kullanım
my_cv = "Python, C#, ASP.NET Core ve SQL konusunda uzman yazılım geliştirici."
job_requirement = "Backend developer position requiring Python, SQL and Cloud knowledge."

score = calculate_cv_match(my_cv, job_requirement)
print(f"Sistem Sonucu: İş ilanıyla uyumluluk oranınız %{score:.2f}")
