from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget,QComboBox
from PyQt5.QtCore import Qt
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registro de Persona')

        # Crear el widget central
        central_widget = QWidget(self)

   
        self.nombre_label = QLabel('Nombre:', self)
        self.nombre_input = QLineEdit(self)

        self.apellido_label = QLabel('Apellido:', self)
        self.apellido_input = QLineEdit(self)

        self.edad_label = QLabel('Edad:', self)
        self.edad_input = QLineEdit(self)

        self.genero_label = QLabel('Género:', self)
        self.genero_input = QComboBox(self)
        self.genero_input.addItems(['Masculino', 'Femenino', 'Otro'])  

        self.email_label = QLabel('Email:', self)
        self.email_input = QLineEdit(self)

        self.telefono_label = QLabel('Teléfono:', self)
        self.telefono_input = QLineEdit(self)

        self.direccion_label = QLabel('Dirección:', self)
        self.direccion_input = QLineEdit(self)

        self.ciudad_label = QLabel('Ciudad:', self)
        self.ciudad_input = QLineEdit(self)

        self.pais_label = QLabel('País:', self)
        self.pais_input = QLineEdit(self)

        self.nacionalidad_label = QLabel('Nacionalidad:', self)
        self.nacionalidad_input = QLineEdit(self)

        self.guardar = QPushButton('Guardar', self)

        self.resultado_label = QLabel('', self)
        self.resultado_label.setAlignment(Qt.AlignCenter)

        # Lista para almacenar el registro
        self.registro = []

        # Configurar el layout
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.apellido_label)
        layout.addWidget(self.apellido_input)
        layout.addWidget(self.edad_label)
        layout.addWidget(self.edad_input)
        layout.addWidget(self.genero_label)
        layout.addWidget(self.genero_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.telefono_label)
        layout.addWidget(self.telefono_input)
        layout.addWidget(self.direccion_label)
        layout.addWidget(self.direccion_input)
        layout.addWidget(self.ciudad_label)
        layout.addWidget(self.ciudad_input)
        layout.addWidget(self.pais_label)
        layout.addWidget(self.pais_input)
        layout.addWidget(self.nacionalidad_label)
        layout.addWidget(self.nacionalidad_input)
        layout.addWidget(self.resultado_label)
        layout.addWidget(self.guardar)

        # Asignar el layout al widget central
        central_widget.setLayout(layout)

        # Establecer el widget central en QMainWindow
        self.setCentralWidget(central_widget)

        # Conectar el botón con la función
        self.guardar.clicked.connect(self.mostra_terminal)

        # Configurar la ventana principal
        self.setGeometry(100, 100, 400, 500)

    def mostra_terminal(self):
        # Obtener los datos de los campos
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        edad = self.edad_input.text()
        genero = self.genero_input.currentText()  # Obtener el valor seleccionado en el QComboBox
        email = self.email_input.text()
        telefono = self.telefono_input.text()
        direccion = self.direccion_input.text()
        ciudad = self.ciudad_input.text()
        pais = self.pais_input.text()
        nacionalidad = self.nacionalidad_input.text()

        # Crear un texto para mostrar los datos
        datos_mostrados = (
            f'Nombre: {nombre}\n'
            f'Apellido: {apellido}\n'
            f'Edad: {edad}\n años'
            f'Género: {genero}\n'
            f'Email: {email}\n'
            f'Teléfono: {telefono}\n'
            f'Dirección: {direccion}\n'
            f'Ciudad: {ciudad}\n'
            f'País: {pais}\n'
            f'Nacionalidad: {nacionalidad}'
        )

        # Mostrar los datos en el QLabel
        self.resultado_label.setText(datos_mostrados)

# Crear la aplicación
app = QApplication(sys.argv)

# Instanciar la ventana y mostrarla
ventana = Ventana()
ventana.show()

# Ejecutar el loop de eventos
sys.exit(app.exec_())

