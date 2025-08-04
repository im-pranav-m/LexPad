from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QFileDialog,
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout
)
import sys

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple PySide6 Text Editor")
        self.setGeometry(100, 100, 800, 600)

        # === Main layout ===
        self.text_edit = QTextEdit()
        layout = QVBoxLayout()

        # Buttons
        button_layout = QHBoxLayout()
        open_btn = QPushButton("Open")
        save_btn = QPushButton("Save")
        open_btn.clicked.connect(self.open_file)
        save_btn.clicked.connect(self.save_file)
        button_layout.addWidget(open_btn)
        button_layout.addWidget(save_btn)

        layout.addLayout(button_layout)
        layout.addWidget(self.text_edit)

        # Central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if path:
            with open(path, "r", encoding="utf-8") as file:
                self.text_edit.setText(file.read())

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if path:
            with open(path, "w", encoding="utf-8") as file:
                file.write(self.text_edit.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())
