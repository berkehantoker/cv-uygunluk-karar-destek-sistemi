import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTextEdit, QPushButton, QLabel, 
                             QFileDialog, QProgressBar, QTableWidget, 
                             QTableWidgetItem, QHeaderView, QMessageBox, QGroupBox)
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt
from worker import ProcessWorker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CV Uygunluk Karar Destek Sistemi - Hibrit Yapay Zeka")
        self.resize(1100, 800) 
        self.pdf_files = []
        self.setup_ui()
        
    def setup_ui(self):
        # Sarı & Koyu Gri Modern Tema Entegrasyonu
        self.setStyleSheet("""
            QMainWindow { background-color: #1c1c1e; }
            QWidget { font-family: 'Segoe UI', Arial, sans-serif; }
            QLabel { color: #e5e5ea; font-size: 14px; font-weight: bold; }
            
            QGroupBox {
                font-weight: bold;
                font-size: 14px;
                border: 1px solid #3a3a3c;
                border-radius: 12px; 
                margin-top: 25px;
                padding-top: 20px;
                background-color: #2c2c2e; 
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 20px;
                padding: 0 5px;
                color: #ffcc00;
                font-size: 15px;
                letter-spacing: 1px;
            }
            
            QTextEdit { 
                background-color: #1c1c1e; 
                color: #ffffff; 
                border: 1px solid #3a3a3c; 
                border-radius: 10px; 
                padding: 12px; 
                font-size: 13px;
                selection-background-color: #ffcc00;
                selection-color: #1c1c1e;
            }
            QTextEdit:focus { border: 1px solid #ffcc00; background-color: #242426; }
            
            QPushButton { 
                background-color: #ffcc00; 
                color: #1c1c1e; 
                border: none; 
                padding: 12px 20px; 
                border-radius: 8px; 
                font-weight: bold; 
                font-size: 14px;
            }
            QPushButton:hover { background-color: #ffd633; }
            QPushButton:pressed { background-color: #e6b800; }
            QPushButton:disabled { background-color: #3a3a3c; color: #636366; }
            
            QProgressBar { 
                border: none; 
                border-radius: 4px; 
                text-align: center; 
                background-color: #2c2c2e;
            }
            QProgressBar::chunk { background-color: #ffcc00; border-radius: 4px;}
            
            QTableWidget { 
                background-color: #1c1c1e; 
                color: #e5e5ea; 
                gridline-color: #3a3a3c; 
                border: 1px solid #3a3a3c; 
                border-radius: 10px; 
                font-size: 13px;
                selection-background-color: #3a3a3c;
                selection-color: #ffffff;
            }
            QHeaderView::section { 
                background-color: #2c2c2e; 
                color: #ffcc00; 
                font-weight: bold; 
                padding: 10px 5px; 
                border: none;
                border-bottom: 2px solid #ffcc00; 
            }
            QTableWidget::item {
                padding: 6px;
                border-bottom: 1px solid #2c2c2e;
            }
            QMessageBox {
                background-color: #2c2c2e;
                color: #e5e5ea;
                border: 1px solid #3a3a3c;
            }
            QMessageBox QPushButton {
                min-width: 90px;
                min-height: 35px;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)

        # ---------------------------------------------------------
        # YAN YANA GİRİŞ ALANLARI (CV ve İş İlanı)
        # ---------------------------------------------------------
        h_layout = QHBoxLayout()

        # SOL TARAF: CV Upload Group (Dikey Ortalanmış)
        cv_group = QGroupBox("CV Dosyaları")
        cv_layout = QVBoxLayout()
        cv_layout.setAlignment(Qt.AlignCenter)

        self.btn_select_file = QPushButton("PDF Dosyalarını Seç")
        self.btn_select_file.setMinimumHeight(50)
        self.btn_select_file.setMinimumWidth(220)
        self.btn_select_file.clicked.connect(self.select_files)

        self.lbl_file_path = QLabel("Seçilen Dosya: Yok")
        self.lbl_file_path.setStyleSheet("color: #8e8e93; font-weight: normal; font-style: italic; padding-top: 10px;")
        self.lbl_file_path.setAlignment(Qt.AlignCenter)

        cv_layout.addWidget(self.btn_select_file)
        cv_layout.addWidget(self.lbl_file_path)
        cv_group.setLayout(cv_layout)

        # SAĞ TARAF: Job Description Group
        job_group = QGroupBox("İş İlanı Metni (İngilizce)")
        job_layout = QVBoxLayout()

        self.job_text_edit = QTextEdit()
        self.job_text_edit.setPlaceholderText("İlan detaylarını buraya yapıştırın...\n\nÖrnek: We are looking for a Data Scientist...")
        self.job_text_edit.setMinimumHeight(150)
        job_layout.addWidget(self.job_text_edit)
        job_group.setLayout(job_layout)

        # Ekrana yan yana (1'e 2 oranında) ekle
        h_layout.addWidget(cv_group, 1)
        h_layout.addWidget(job_group, 2)
        
        main_layout.addLayout(h_layout)

        # ---------------------------------------------------------
        # ALT BUTONLAR (Analiz Başlat)
        # ---------------------------------------------------------
        control_layout = QHBoxLayout()
        
        self.btn_start = QPushButton("Analizi Başlat")
        self.btn_start.setMinimumHeight(45)
        self.btn_start.clicked.connect(self.start_analysis)
        self.btn_start.setEnabled(False)

        control_layout.addWidget(self.btn_start)
        main_layout.addLayout(control_layout)

        # Yükleme Çubuğu (Daha ince ve modern)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setFixedHeight(8) 
        self.progress_bar.setTextVisible(False)
        main_layout.addWidget(self.progress_bar)

        # ---------------------------------------------------------
        # SONUÇ TABLOSU
        # ---------------------------------------------------------
        self.table = QTableWidget()
        self.table.setColumnCount(4) 
        self.table.setHorizontalHeaderLabels(["CV Dosya Adı", "TF-IDF Skoru (%)", "BERT Skoru (%)", "Nihai Skor (%)"])
        
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        main_layout.addWidget(self.table)

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "CV PDF Dosyalarını Seçin", "", "PDF Dosyaları (*.pdf)")
        if files:
            self.pdf_files = files
            if len(files) == 1:
                self.lbl_file_path.setText(f"Seçilen: {os.path.basename(files[0])}")
                self.lbl_file_path.setStyleSheet("color: #ffcc00; font-weight: bold; padding-top: 10px;")
            else:
                self.lbl_file_path.setText(f"Seçilen: {len(files)} dosya")
                self.lbl_file_path.setStyleSheet("color: #ffcc00; font-weight: bold; padding-top: 10px;")
            self.btn_start.setEnabled(True)

    def start_analysis(self):
        job_text = self.job_text_edit.toPlainText().strip()
        
        if not job_text:
            QMessageBox.warning(self, "Eksik Bilgi", "Lütfen önce bir iş ilanı metni girin!")
            return

        self.table.setRowCount(0)
        self.progress_bar.setValue(0)
        self.btn_start.setEnabled(False)
        self.btn_select_file.setEnabled(False)

        self.worker = ProcessWorker(job_text, self.pdf_files)
        self.worker.progress.connect(self.update_progress)
        self.worker.result.connect(self.add_result_to_table)
        self.worker.finished_signal.connect(self.analysis_finished)
        self.worker.start()

    def update_progress(self, val):
        self.progress_bar.setValue(val)

    def add_result_to_table(self, filename, tfidf_score, bert_score, final_score):
        row = self.table.rowCount()
        self.table.insertRow(row)

        item_name = QTableWidgetItem(filename)
        self.table.setItem(row, 0, item_name)

        # Skorlara göre dinamik renk ataması (Koyu temaya uyumlu)
        scores = [tfidf_score, bert_score, final_score]
        for col_index, score in enumerate(scores, start=1):
            item_score = QTableWidgetItem(f"% {score:.2f}")
            item_score.setTextAlignment(Qt.AlignCenter)
            
            font = QFont()
            font.setBold(True)
            item_score.setFont(font)

            if score >= 65.0:
                bg_color = QColor("#198754")  # Yeşil
                text_color = QColor("white")
            elif score >= 40.0:
                bg_color = QColor("#ffc107")  # Sarı
                text_color = QColor("white")
            else:
                bg_color = QColor("#dc3545")  # Kırmızı
                text_color = QColor("white")

            item_score.setBackground(bg_color)
            item_score.setForeground(text_color)
            self.table.setItem(row, col_index, item_score)

    def analysis_finished(self):
        self.btn_start.setEnabled(True)
        self.btn_select_file.setEnabled(True)
        
        self.table.sortItems(3, Qt.DescendingOrder)
        QMessageBox.information(self, "İşlem Tamam", "CV Analizi başarıyla tamamlandı!\nSonuçları tablodan inceleyebilirsiniz.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
