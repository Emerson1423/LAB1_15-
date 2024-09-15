from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import sys

class Ventana(QMainWindow):  # Usamos QMainWindow en lugar de QWidget
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejercicio 2')
        
        
        central_widget = QWidget(self)  # Necesitamos un widget central en QMainWindow

        
        self.password_label = QLabel('Contraseña:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)  # Ocultar el texto de la contraseña
        self.login_button = QPushButton('Iniciar sesión', self)

        # Configurar el layout
        layout = QVBoxLayout()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        central_widget.setLayout(layout)

        # Establecer el widget central en QMainWindow
        self.setCentralWidget(central_widget)

        # Conectar el botón con la función
        self.login_button.clicked.connect(self.mostra_terminal)

        # Configurar la ventana principal
        self.setGeometry(100, 100, 300, 100)

    def mostra_terminal(self):
        password = self.password_input.text()
        print(f'Contraseña: {password}')


# Crear la aplicación
app = QApplication(sys.argv)

# Instanciar la ventana y mostrarla
ventana = Ventana()
ventana.show()

# Ejecutar el loop de eventos
sys.exit(app.exec_())
