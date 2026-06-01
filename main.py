import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTextEdit, QFileDialog, QProgressBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QMessageBox, QGroupBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Diğer katmanlardaki gerekli yapıları temiz bir mimariyle içeri alıyoruz
from utils import extract_text_from_pdf
from worker import AnalysisWorker


class ResumeMatcherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cv_text = ""
        self.job_text = ""
        self.worker = None
        self.results = None

        self.init_ui()

    def init_ui(self):
        """Initialize user interface"""
        self.setWindowTitle("Resume - Job Matching Sistemi")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet(self.get_stylesheet())

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Title
        title = QLabel("CV - İş İlanı Uyum Analiz Sistemi")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #ffffff; margin-bottom: 10px;")
        layout.addWidget(title)

        # Tabs
        tabs = QTabWidget()
        
        # Tab 1: Upload and Job Description
        tab1 = self.create_input_tab()
        tabs.addTab(tab1, "Giriş (Input)")

        # Tab 2: Results
        tab2 = self.create_results_tab()
        tabs.addTab(tab2, "Sonuçlar")

        layout.addWidget(tabs)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setFixedHeight(6)
        self.progress_bar.setTextVisible(False)
        layout.addWidget(self.progress_bar)

        # Status label
        self.status_label = QLabel("Hazır")
        self.status_label.setStyleSheet("color: #4ade80; font-weight: bold; font-size: 12px;")
        layout.addWidget(self.status_label)

    def create_input_tab(self):
        """Create input tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # CV Upload Group
        cv_group = QGroupBox("CV Dosyası")
        cv_layout = QHBoxLayout()

        self.cv_label = QLabel("Dosya seçilmedi")
        self.cv_label.setStyleSheet("color: #9ca3af; padding: 10px;")

        self.cv_button = QPushButton("PDF Dosyasını Yükle")
        self.cv_button.setMinimumHeight(45)
        self.cv_button.clicked.connect(self.load_cv)

        cv_layout.addWidget(self.cv_label)
        cv_layout.addWidget(self.cv_button)
        cv_group.setLayout(cv_layout)
        layout.addWidget(cv_group)

        # Job Description Group
        job_group = QGroupBox("İş İlanı Metni")
        job_layout = QVBoxLayout()

        self.job_text_edit = QTextEdit()
        self.job_text_edit.setPlaceholderText(
            "İş ilanı metnini buraya yapıştırın veya yazın...\n\n"
            "Örnek: We are looking for a Python developer with SQL and Machine Learning skills..."
        )
        self.job_text_edit.setMinimumHeight(250)

        job_layout.addWidget(self.job_text_edit)
        job_group.setLayout(job_layout)
        layout.addWidget(job_group)

        # Analyze button
        self.analyze_button = QPushButton("Analiz Başlat")
        self.analyze_button.setMinimumHeight(50)
        self.analyze_button.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.analyze_button.clicked.connect(self.start_analysis)
        layout.addWidget(self.analyze_button)

        layout.addStretch()
        return widget

    def create_results_tab(self):
        """Create results tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Scores Group
        scores_group = QGroupBox("Eşleşme Puanları")
        scores_layout = QHBoxLayout()

        self.text_sim_label = QLabel("Metin Benzerliği: --")
        self.text_sim_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.text_sim_label.setStyleSheet("padding: 15px; background-color: #1e1e1e; border: 1px solid #333333; border-radius: 8px; color: #ffffff;")
        self.text_sim_label.setAlignment(Qt.AlignCenter)

        self.skill_match_label = QLabel("Beceri Uyumu: --")
        self.skill_match_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.skill_match_label.setStyleSheet("padding: 15px; background-color: #1e1e1e; border: 1px solid #333333; border-radius: 8px; color: #ffffff;")
        self.skill_match_label.setAlignment(Qt.AlignCenter)

        scores_layout.addWidget(self.text_sim_label)
        scores_layout.addWidget(self.skill_match_label)
        scores_group.setLayout(scores_layout)
        layout.addWidget(scores_group)

        # Skills Tables
        tables_layout = QHBoxLayout()

        # Required Skills
        req_skills_group = QGroupBox("Gereken Beceriler")
        req_skills_layout = QVBoxLayout()
        self.required_skills_table = QTableWidget()
        self.required_skills_table.setColumnCount(1)
        self.required_skills_table.setHorizontalHeaderLabels(["Beceri"])
        self.required_skills_table.horizontalHeader().setStretchLastSection(True)
        req_skills_layout.addWidget(self.required_skills_table)
        req_skills_group.setLayout(req_skills_layout)
        tables_layout.addWidget(req_skills_group)

        # Found Skills
        found_skills_group = QGroupBox("CV'de Bulunan Beceriler")
        found_skills_layout = QVBoxLayout()
        self.found_skills_table = QTableWidget()
        self.found_skills_table.setColumnCount(1)
        self.found_skills_table.setHorizontalHeaderLabels(["Beceri"])
        self.found_skills_table.horizontalHeader().setStretchLastSection(True)
        found_skills_layout.addWidget(self.found_skills_table)
        found_skills_group.setLayout(found_skills_layout)
        tables_layout.addWidget(found_skills_group)

        # Missing Skills
        missing_skills_group = QGroupBox("Eksik Beceriler")
        missing_skills_layout = QVBoxLayout()
        self.missing_skills_table = QTableWidget()
        self.missing_skills_table.setColumnCount(1)
        self.missing_skills_table.setHorizontalHeaderLabels(["Beceri"])
        self.missing_skills_table.horizontalHeader().setStretchLastSection(True)
        missing_skills_layout.addWidget(self.missing_skills_table)
        missing_skills_group.setLayout(missing_skills_layout)
        tables_layout.addWidget(missing_skills_group)

        layout.addLayout(tables_layout)
        return widget

    def load_cv(self):
        """Load CV from file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "PDF Dosyasını Seçin", "", "PDF Files (*.pdf)"
        )

        if file_path:
            try:
                self.cv_text = extract_text_from_pdf(file_path)
                self.cv_label.setText(f"Yüklendi: {os.path.basename(file_path)}")
                self.cv_label.setStyleSheet("color: #4ade80; padding: 10px; font-weight: bold;")
                self.status_label.setText("CV yüklendi. İş ilanını yazın ve analiz başlatın.")
                self.status_label.setStyleSheet("color: #4ade80; font-weight: bold;")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"PDF okunamadı:\n{str(e)}")
                self.status_label.setText("PDF okuma hatası!")
                self.status_label.setStyleSheet("color: #f87171; font-weight: bold;")

    def start_analysis(self):
        """Start analysis"""
        self.job_text = self.job_text_edit.toPlainText().strip()

        if not self.cv_text:
            QMessageBox.warning(self, "Uyarı", "Lütfen önce CV dosyasını yükleyin!")
            return

        if not self.job_text:
            QMessageBox.warning(self, "Uyarı", "Lütfen iş ilanı metnini yazın!")
            return

        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.analyze_button.setEnabled(False)
        self.status_label.setText("Analiz yapılıyor...")
        self.status_label.setStyleSheet("color: #fbbf24; font-weight: bold;")

        # Start worker thread
        self.worker = AnalysisWorker(self.cv_text, self.job_text)
        self.worker.progress.connect(self.on_progress)
        self.worker.finished.connect(self.on_analysis_finished)
        self.worker.error.connect(self.on_analysis_error)
        self.worker.start()

    def on_progress(self, message):
        """Update progress"""
        self.status_label.setText(message)
        self.progress_bar.setValue(self.progress_bar.value() + 25)

    def on_analysis_finished(self, results):
        """Display results"""
        self.results = results

        # Update scores
        text_sim = results["text_similarity"]
        skill_match = results["skill_match"]

        # Color coding for scores
        text_sim_color = self.get_score_color(text_sim)
        skill_match_color = self.get_score_color(skill_match)

        self.text_sim_label.setText(f"Metin Benzerliği: {text_sim:.2f}%")
        self.text_sim_label.setStyleSheet(f"padding: 15px; background-color: {text_sim_color}; border-radius: 8px; color: #ffffff; font-weight: bold; border: none;")

        self.skill_match_label.setText(f"Beceri Uyumu: {skill_match:.2f}%")
        self.skill_match_label.setStyleSheet(f"padding: 15px; background-color: {skill_match_color}; border-radius: 8px; color: #ffffff; font-weight: bold; border: none;")

        # Populate tables
        self.populate_table(self.required_skills_table, results["required_skills"])
        self.populate_table(self.found_skills_table, results["found_skills"])
        self.populate_table(self.missing_skills_table, results["missing_skills"])

        self.progress_bar.setVisible(False)
        self.analyze_button.setEnabled(True)
        self.status_label.setText("Analiz tamamlandı!")
        self.status_label.setStyleSheet("color: #4ade80; font-weight: bold;")

        QMessageBox.information(self, "Başarılı", "Analiz tamamlandı! Sonuçları 'Sonuçlar' sekmesinde görebilirsiniz.")

    def on_analysis_error(self, error_message):
        """Handle analysis error"""
        self.progress_bar.setVisible(False)
        self.analyze_button.setEnabled(True)
        self.status_label.setText(error_message)
        self.status_label.setStyleSheet("color: #f87171; font-weight: bold;")
        QMessageBox.critical(self, "Hata", error_message)

    def populate_table(self, table, items):
        """Fill table with items"""
        table.setRowCount(len(items))
        for row, item in enumerate(items):
            table.setItem(row, 0, QTableWidgetItem(item))

    def get_score_color(self, score):
        """Get color based on score (Dark theme optimized)"""
        if score >= 75:
            return "#16a34a"  # Modern Green
        elif score >= 50:
            return "#d97706"  # Modern Amber/Orange
        else:
            return "#dc2626"  # Modern Red

    def get_stylesheet(self):
        """Return custom modern dark stylesheet"""
        return """
        QMainWindow {
            background-color: #121212;
            color: #e0e0e0;
        }
        QWidget {
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #e0e0e0;
        }
        QGroupBox {
            font-weight: bold;
            font-size: 14px;
            border: 1px solid #333333;
            border-radius: 8px;
            margin-top: 20px;
            padding-top: 15px;
            background-color: #1e1e1e;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            left: 15px;
            padding: 0 5px;
            color: #9ca3af;
        }
        QTextEdit, QTableWidget {
            background-color: #121212;
            color: #e0e0e0;
            border: 1px solid #333333;
            border-radius: 6px;
            padding: 8px;
            selection-background-color: #2563eb;
        }
        QHeaderView::section {
            background-color: #2c2c2c;
            color: #ffffff;
            padding: 5px;
            border: none;
            border-bottom: 1px solid #444444;
            font-weight: bold;
        }
        QTableWidget::item {
            padding: 5px;
            border-bottom: 1px solid #2a2a2a;
        }
        QPushButton {
            background-color: #2563eb;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 10px 15px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #3b82f6;
        }
        QPushButton:pressed {
            background-color: #1d4ed8;
        }
        QPushButton:disabled {
            background-color: #374151;
            color: #9ca3af;
        }
        QTabWidget::pane {
            border: 1px solid #333333;
            background-color: #1e1e1e;
            border-radius: 8px;
        }
        QTabBar::tab {
            background-color: #121212;
            color: #9ca3af;
            padding: 12px 25px;
            margin-right: 2px;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            border: 1px solid #333333;
            border-bottom: none;
        }
        QTabBar::tab:selected {
            background-color: #1e1e1e;
            color: #ffffff;
            font-weight: bold;
            border-bottom: 2px solid #2563eb;
        }
        QTabBar::tab:hover:!selected {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        QProgressBar {
            border: none;
            background-color: #333333;
            border-radius: 3px;
        }
        QProgressBar::chunk {
            background-color: #3b82f6;
            border-radius: 3px;
        }
        QMessageBox {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResumeMatcherApp()
    window.show()
    sys.exit(app.exec_())