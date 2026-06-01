from PyQt5.QtCore import QThread, pyqtSignal
# Üstteki utils dosyasından çekirdek NLP fonksiyonlarını içe aktarıyoruz
from utils import clean_text, calculate_text_similarity, analyze_skills


class AnalysisWorker(QThread):
    """Background thread for analysis to keep UI responsive"""
    progress = pyqtSignal(str)
    finished = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, cv_text, job_text):
        super().__init__()
        self.cv_text = cv_text
        self.job_text = job_text

    def run(self):
        try:
            self.progress.emit("Text preprocessing başlanıyor...")
            cleaned_cv = clean_text(self.cv_text)
            cleaned_job = clean_text(self.job_text)

            self.progress.emit("TF-IDF similarity calculation...")
            text_similarity = calculate_text_similarity(cleaned_cv, cleaned_job)

            self.progress.emit("Skill matching yapılıyor...")
            required_skills, found_skills, missing_skills, skill_match_score, missing_df = analyze_skills(
                cleaned_cv, cleaned_job
            )

            results = {
                "text_similarity": text_similarity,
                "skill_match": skill_match_score,
                "required_skills": required_skills,
                "found_skills": found_skills,
                "missing_skills": missing_skills,
                "missing_df": missing_df
            }

            self.progress.emit("Analiz tamamlandı!")
            self.finished.emit(results)

        except Exception as e:
            self.error.emit(f"Hata: {str(e)}")