"""
BulkMailer Pro - Main Entry Point
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QFontDatabase

from ui.app import BulkMailerApp


def main():
    # Enable high DPI
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName("BulkMailer Pro")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("BulkMailer")

    # Set default font
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    window = BulkMailerApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
