import sys

from PySide2.QtWidgets import QApplication

from AlgoritmodO.Front_shi import Front

def main():
    app = QApplication(sys.argv)
    window = Front.MainWindow()
    window.show()
    sys.exit(app.exec_())






