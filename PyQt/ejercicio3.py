from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejercicio 2')

       
        central_widget = QWidget(self)  

       
        self.cedula_label = QLabel('Cédula:', self)
        self.cedula_input = QLineEdit(self)

        self.nombre_label = QLabel('Nombre Completo:', self)
        self.nombre_input = QLineEdit(self)


        self.guardar = QPushButton('guardar', self)

        # Alinear las etiquetas al centro
        self.cedula_label.setAlignment(Qt.AlignCenter)
        self.nombre_label.setAlignment(Qt.AlignCenter)

        # Configurar el layout
        layout = QVBoxLayout()
        layout.addWidget(self.cedula_label)
        layout.addWidget(self.cedula_input)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.guardar)

        # Asignar el layout al widget central
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        # Conectar el botón con la función
        self.guardar.clicked.connect(self.mostra_terminal)

        # Configurar la ventana principal
        self.setGeometry(100, 100, 400, 200)  # Ajusté el tamaño para acomodar todos los campos

    def mostra_terminal(self):
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()
        print(f'Cédula: {cedula}')
        print(f'Nombre Completo: {nombre}')

# Crear la aplicación
app = QApplication(sys.argv)

# Instanciar la ventana y mostrarla
ventana = Ventana()
ventana.show()

# Ejecutar el loop de eventos
sys.exit(app.exec())
