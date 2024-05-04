import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from AlgoritmodO.Back_shi import Creador, Usuario
import pandas as pd
import requests


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ordenamiento de Datos")
        self.layout = QVBoxLayout()

        self.metodo_label = QLabel("Método de Ordenamiento:")
        self.metodo_combo = QComboBox()
        self.metodo_combo.addItems(["1 - Merge", "2 - Heap", "3 - Radix", "4 - Selection", "5 - Bubble", "6 - Counting", "7 - Insertion", "8 - Quick", "9 - Bucket"])

        self.columna_label = QLabel("Columna:")
        self.columna_edit = QLineEdit()

        self.ordenar_button = QPushButton("Ordenar")
        self.ordenar_button.clicked.connect(self.ordenar_datos)

        self.resultado_label = QLabel("")

        self.layout.addWidget(self.metodo_label)
        self.layout.addWidget(self.metodo_combo)
        self.layout.addWidget(self.columna_label)
        self.layout.addWidget(self.columna_edit)
        self.layout.addWidget(self.ordenar_button)
        self.layout.addWidget(self.resultado_label)

        self.setLayout(self.layout)

        self.mostrar_columnas_disponibles()

    def mostrar_columnas_disponibles(self):
        ruta = "https://www.datos.gov.co/resource/dyy8-9s4r.json"
        datos = requests.get(ruta)
        datos_json = datos.json()
        columnas_disponibles = pd.json_normalize(datos_json).columns.tolist()
        QMessageBox.information(self, "Columnas Disponibles",
                                f"Las columnas disponibles son: {', '.join(columnas_disponibles)}")

    def ordenar_datos(self):
        metodo_elegido = int(self.metodo_combo.currentText().split()[0])
        columna = self.columna_edit.text().lower()  # Convertir a minúsculas
        ruta = "https://www.datos.gov.co/resource/dyy8-9s4r.json"

        try:
            if columna not in ['hombres', 'mujeres', 'edad']:
                raise ValueError("La columna debe ser 'hombres', 'mujeres' o 'edad'")

            datos = requests.get(ruta)
            datos_json = datos.json()
            datos_df = pd.json_normalize(datos_json)
            ordenamiento = datos_df[columna]
            ordenamiento = ordenamiento.astype(int)

            metodo = Usuario.Usuario.obtener_metodo_ordenamiento(metodo_elegido)
            if metodo is not None:
                creator = Creador.Creator()
                array_ordenado, mensaje = creator.ordenar(metodo_elegido, ordenamiento, columna)

                self.resultado_label.setText(f"Array Ordenado:\n {array_ordenado}\n{mensaje}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
