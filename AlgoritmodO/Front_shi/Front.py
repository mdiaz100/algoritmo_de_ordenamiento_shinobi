import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QScrollArea, QMessageBox
from AlgoritmodO.Back_shi import Creador, Usuario
import pandas as pd
import requests
from AlgoritmodO.Front_shi import Registro



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
        self.resultado_scroll_area = QScrollArea()
        self.resultado_scroll_area.setWidgetResizable(True)
        self.resultado_scroll_area.setWidget(self.resultado_label)

        self.layout.addWidget(self.metodo_label)
        self.layout.addWidget(self.metodo_combo)
        self.layout.addWidget(self.columna_label)
        self.layout.addWidget(self.columna_edit)
        self.layout.addWidget(self.ordenar_button)
        self.layout.addWidget(self.resultado_scroll_area)

        self.setLayout(self.layout)

        self.mostrar_columnas_disponibles()

    def mostrar_columnas_disponibles(self):
        ruta = "https://www.datos.gov.co/resource/bgwm-xwyw.json"
        datos = requests.get(ruta)
        datos_json = datos.json()
        columnas_disponibles = pd.json_normalize(datos_json).columns.tolist()

    def ordenar_datos(self):
        metodo_elegido = int(self.metodo_combo.currentText().split()[0])
        columna = self.columna_edit.text().lower()  # Convertir a minúsculas
        ruta = "https://www.datos.gov.co/resource/bgwm-xwyw.json"

        try:
            if columna not in ['peso', 'talla_', 'tiempo_gestaci_n_']:
                raise ValueError("La columna debe ser 'peso', 'talla_' o 'tiempo_gestaci_n_'")

            datos = requests.get(ruta)
            datos_json = datos.json()
            datos_df = pd.json_normalize(datos_json)
            ordenamiento = datos_df[columna]
            ordenamiento = ordenamiento.astype(int)
            metodo = Usuario.Usuario.obtener_metodo_ordenamiento(metodo_elegido)
            data = []
            for _, row in datos_df.iterrows():
                registro = Registro.Registro(
                    row["ficha_de_informaci_n_publicaci"],
                    row["sexo"],
                    row["peso"],
                    row["talla_"],
                    row["parto_atendido"],
                    row["tiempo_gestaci_n_"],
                    row["n_mero_consultas_prenatales"],
                    row["tipo_parto"],
                    row["mutiplicidad_"],
                    row["apgar1"],
                    row["apgar2"],
                    row["grupo_sangu_neo_"],
                    row["factor_rh"],
                    row["pertenencia_tnica_"],
                    row["estado_conyugal_madre"],
                    row["nivel_educativo_"],
                    row["pa_s_de_residencia_"],
                    row["municipio_"],
                    row["_rea_residencia_"],
                    row["n_mero_hijos_nacidos_vivos_"],
                    row["r_gimen_seguridad_"],
                    row["nombre_administradora_"],
                    row["nivel_educativo_padre"]
                )
                data.append(registro)

            if metodo is not None:
                creator = Creador.Creator()
                array_ordenado= creator.ordenar(metodo_elegido, data, columna)

                array_str = "\n".join(map(str, array_ordenado))

                self.resultado_label.setText(f"Array Ordenado:\n {array_str}")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

