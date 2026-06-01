import os
import re
import pandas as pd
import nltk
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# NLTK SETUP
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

from nltk.corpus import stopwords


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF resume"""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    reader = PdfReader(pdf_path)
    extracted_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            extracted_text += text + "\n"

    return extracted_text


def normalize_technical_terms(text):
    """Normalize technical terms"""
    text = text.lower()

    replacements = {
        "c#": "csharp",
        "c #": "csharp",
        "c++": "cplusplus",
        "c ++": "cplusplus",
        ".net": "dotnet",
        "dot net": "dotnet",
        "asp.net": "aspnet",
        "asp .net": "aspnet",
        "asp. net": "aspnet",
        "asp . net": "aspnet",
        "node.js": "nodejs",
        "node js": "nodejs",
        "react.js": "reactjs",
        "react js": "reactjs",
        "vue.js": "vuejs",
        "vue js": "vuejs",
        "next.js": "nextjs",
        "next js": "nextjs",
        "scikit-learn": "scikit learn",
        "machine-learning": "machine learning",
        "deep-learning": "deep learning",
        "natural-language-processing": "natural language processing",
        "data-science": "data science",
        "data-analysis": "data analysis",
        "computer-vision": "computer vision",
        "rest-api": "rest api"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def clean_text(text):
    """Clean and preprocess text"""
    text = normalize_technical_terms(text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    words = text.split()

    english_stopwords = set(stopwords.words("english"))

    custom_stopwords = {
        "resume", "cv", "curriculum", "vitae",
        "email", "phone", "address", "linkedin", "github",
        "candidate", "applicant", "job", "role", "position",
        "company", "team", "project", "projects",
        "required", "requirement", "requirements",
        "responsibility", "responsibilities",
        "experience", "knowledge", "skills", "skill",
        "ability", "good", "strong", "excellent",
        "working", "work", "development", "developer",
        "engineer", "engineering", "computer",
        "university", "education", "department",
        "looking", "preferred", "plus", "using", "based"
    }

    all_stopwords = english_stopwords.union(custom_stopwords)

    cleaned_words = [
        word for word in words
        if word not in all_stopwords and len(word) > 1
    ]

    return " ".join(cleaned_words)


def calculate_text_similarity(cv_cleaned, job_cleaned):
    """Calculate TF-IDF similarity"""
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 3),
        token_pattern=r"(?u)\b\w+\b"
    )

    tfidf_matrix = vectorizer.fit_transform([cv_cleaned, job_cleaned])
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return similarity_matrix[0][0] * 100


def skill_exists(text, skill):
    """Check if skill exists as complete term"""
    pattern = r'(?<!\w)' + re.escape(skill) + r'(?!\w)'
    return re.search(pattern, text) is not None


def analyze_skills(cv_cleaned, job_cleaned):
    """Analyze skills"""
    target_skills = {
        "python": "Python",
        "java": "Java",
        "javascript": "JavaScript",
        "typescript": "TypeScript",
        "csharp": "C#",
        "cplusplus": "C++",
        "dotnet": ".NET",
        "aspnet": "ASP.NET",
        "mvc": "MVC",
        "entity framework": "Entity Framework",
        "sql": "SQL",
        "mysql": "MySQL",
        "postgresql": "PostgreSQL",
        "mongodb": "MongoDB",
        "git": "Git",
        "html": "HTML",
        "css": "CSS",
        "bootstrap": "Bootstrap",
        "react": "React",
        "reactjs": "React.js",
        "angular": "Angular",
        "vuejs": "Vue.js",
        "nodejs": "Node.js",
        "machine learning": "Machine Learning",
        "deep learning": "Deep Learning",
        "natural language processing": "Natural Language Processing",
        "nlp": "NLP",
        "computer vision": "Computer Vision",
        "data science": "Data Science",
        "data analysis": "Data Analysis",
        "pandas": "Pandas",
        "numpy": "NumPy",
        "scikit learn": "Scikit-learn",
        "tensorflow": "TensorFlow",
        "pytorch": "PyTorch",
        "aws": "AWS",
        "azure": "Azure",
        "cloud": "Cloud",
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "rest api": "REST API",
    }

    required_skills = []
    found_skills = []
    missing_skills = []

    for normalized_skill, display_name in target_skills.items():
        if skill_exists(job_cleaned, normalized_skill):
            required_skills.append(display_name)

            if skill_exists(cv_cleaned, normalized_skill):
                found_skills.append(display_name)
            else:
                missing_skills.append(display_name)

    if len(required_skills) > 0:
        skill_match_score = (len(found_skills) / len(required_skills)) * 100
    else:
        skill_match_score = 0.0

    if missing_skills:
        missing_skills_report = pd.DataFrame(
            missing_skills,
            columns=["Missing Technical Skills"]
        )
    else:
        missing_skills_report = pd.DataFrame(
            ["Eksik teknik beceri bulunamadı."],
            columns=["Status"]
        )

    return required_skills, found_skills, missing_skills, skill_match_score, missing_skills_report