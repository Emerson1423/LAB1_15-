from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejercicio 2')

        # Crear el widget central
        central_widget = QWidget(self)  # Necesitamos un widget central en QMainWindow

      
        self.nombre_label = QLabel('Nombre del animal:', self)
        self.nombre_input = QLineEdit(self)

        self.tipo_label = QLabel('tipo de animal:', self)
        self.tipo_input = QLineEdit(self)

        self.peso_label = QLabel('Peso:', self)
        self.peso_input = QLineEdit(self)

        self.edad_label = QLabel('Edad:', self)
        self.edad_input = QLineEdit(self)

        self.guardar = QPushButton('Guardar', self)

        self.resultado_label = QLabel('', self)
        self.resultado_label.setAlignment(Qt.AlignCenter)

        # Lista para almacenar los registros
        self.registros = []

        # Configurar el layout
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.tipo_label)
        layout.addWidget(self.tipo_input)
        layout.addWidget(self.peso_label)
        layout.addWidget(self.peso_input)
        layout.addWidget(self.edad_label)
        layout.addWidget(self.edad_input)
        layout.addWidget(self.resultado_label)
        layout.addWidget(self.guardar)

        # Asignar el layout al widget central
        central_widget.setLayout(layout)

        # Establecer el widget central en QMainWindow
        self.setCentralWidget(central_widget)

        # Conectar el botón con la función
        self.guardar.clicked.connect(self.mostra_terminal)

        # Configurar la ventana principal
        self.setGeometry(100, 100, 400, 300)  # Ajusté el tamaño para acomodar todos los campos

    def mostra_terminal(self):
        # Obtener los datos de los campos
        nombre = self.nombre_input.text()
        tipo = self.tipo.text()
        peso = self.peso_input.text()
        edad = self.edad_input.text()

        # Crear un texto para mostrar los datos
        registro = f'Nombre: {nombre}\ntipo de animal: {tipo}\nPeso: {peso}\nEdad: {edad}'
        
        # Almacenar el nuevo registro
        self.registros.append(registro)

        # Mostrar solo los tres registros más recientes
        if len(self.registros) > 3:
            self.registros = self.registros[-3:]

        # Unir los registros en un solo texto para mostrar
        datos_mostrados = '\n\n'.join(self.registros)

      
        self.resultado_label.setText(datos_mostrados)


app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()


sys.exit(app.exec())




