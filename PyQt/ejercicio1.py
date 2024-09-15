from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QVBoxLayout,QWidget
from PyQt5.QtCore import Qt

import sys

class Ventana(QMainWindow):  # Usamos QMainWindow en lugar de QWidget
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejercicio 1')
        
        # Crear un widget central
        central_widget = QWidget(self)
        
        # Crear los QLabel
        label_nombre = QLabel('Nombre: Emerson Aldahir Portillo Segovia', self)
        label_edad = QLabel('Edad: 20', self)

        # Alinear los textos al centro
        label_nombre.setAlignment(Qt.AlignCenter)
        label_edad.setAlignment(Qt.AlignCenter)

        # Crear un layout y añadir los QLabel
        layout = QVBoxLayout()
        layout.addWidget(label_nombre)
        layout.addWidget(label_edad)

        # Establecer el layout en el widget central
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Añadir el layout al widget principal
        


        
        

        


# Crear la aplicación
app = QApplication(sys.argv)

# Instanciar la ventana y mostrarla
ventana = Ventana()
ventana.show()

# Ejecutar el loop de eventos
sys.exit(app.exec())
