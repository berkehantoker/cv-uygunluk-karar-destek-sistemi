import re
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

print("İngilizce Yapay Zeka (BERT) Modeli yükleniyor...")
bert_model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model başarıyla yüklendi!")

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + " "
    except Exception as e:
        print(f"PDF Okuma Hatası ({pdf_path}): {e}")
    return text.strip()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s\.\+#-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def calculate_hybrid_similarity(job_desc, cv_text, bert_weight=0.7, tfidf_weight=0.3):
    # 1. TF-IDF HESAPLAMASI (Kelime)
    try:
        vectorizer = TfidfVectorizer(ngram_range=(1, 3))
        tfidf_matrix = vectorizer.fit_transform([job_desc, cv_text])
        tfidf_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100
    except ValueError:
        tfidf_score = 0.0

    # 2. BERT HESAPLAMASI (Anlam)
    job_embedding = bert_model.encode(job_desc, convert_to_tensor=True)
    cv_embedding = bert_model.encode(cv_text, convert_to_tensor=True)
    bert_score = util.cos_sim(job_embedding, cv_embedding).item() * 100
    bert_score = max(bert_score, 0)

    # 3. NİHAİ SKOR
    final_score = (bert_score * bert_weight) + (tfidf_score * tfidf_weight)
    
    # Üç skoru da yuvarlayıp geri döndürüyoruz
    return round(tfidf_score, 2), round(bert_score, 2), round(final_score, 2)
