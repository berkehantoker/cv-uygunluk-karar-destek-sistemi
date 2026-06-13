import os
from PyQt5.QtCore import QThread, pyqtSignal
from utils import extract_text_from_pdf, preprocess_text, calculate_hybrid_similarity

class ProcessWorker(QThread):
    progress = pyqtSignal(int)
    # Sinyali güncelledik: Dosya adı ve 3 ayrı float (sayısal) değer gönderecek
    result = pyqtSignal(str, float, float, float)
    finished_signal = pyqtSignal()

    def __init__(self, job_text, pdf_files):
        super().__init__()
        self.job_text = job_text
        self.pdf_files = pdf_files

    def run(self):
        total_files = len(self.pdf_files)

        if total_files == 0:
            self.finished_signal.emit()
            return

        clean_job_text = preprocess_text(self.job_text)

        for i, file_path in enumerate(self.pdf_files):
            filename = os.path.basename(file_path)
            
            raw_cv_text = extract_text_from_pdf(file_path)
            clean_cv_text = preprocess_text(raw_cv_text)

            if clean_cv_text:
                # utils'den gelen 3 değeri alıyoruz
                tfidf_score, bert_score, final_score = calculate_hybrid_similarity(clean_job_text, clean_cv_text)
            else:
                tfidf_score, bert_score, final_score = 0.0, 0.0, 0.0

            # Arayüze 3 skoru birden yolluyoruz
            self.result.emit(filename, tfidf_score, bert_score, final_score)
            
            progress_percent = int(((i + 1) / total_files) * 100)
            self.progress.emit(progress_percent)

        self.finished_signal.emit()
