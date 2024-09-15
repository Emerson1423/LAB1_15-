import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget, QFormLayout

class EmployeeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Registro de Empleados')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        form_layout = QFormLayout()

       
        self.nombre_input = QLineEdit()
        self.sueldo_input = QLineEdit()

        form_layout.addRow("Nombre del Empleado", self.nombre_input)
        form_layout.addRow("Sueldo del Empleado", self.sueldo_input)

     
        self.add_button = QPushButton("Agregar Empleado")
        self.add_button.clicked.connect(self.agregaremplado)

        
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(QLabel("Resumen de los Trabajadores:"))
        main_layout.addWidget(self.result_output)

        central_widget.setLayout(main_layout)

        # Lista para almacenar los datos de los empleados
        self.empleados = []

    def agregaremplado(self):
        # Permite registrar hasta 3 empleados
        if len(self.empleados) >= 3:
            self.result_output.append("Ya has registrado 3 empleados.\n")
            return

        try:
            # Tomar los valores ingresados
            nombre = self.nombre_input.text()
            sueldo = float(self.sueldo_input.text())
            renta = self.calcularrenta(sueldo)
            sueldo_neto = sueldo - renta

           
            empleado_data = {
                "Nombre": nombre,
                "Sueldo": sueldo,
                "Renta": renta,
                "Sueldo Neto": sueldo_neto
            }
            self.empleados.append(empleado_data)

            # Mostrar los resultados acumulados
            self.result_output.clear() 
            for empleado in self.empleados:
                resumen = (f"Nombre: {empleado['Nombre']}\n"
                           f"Sueldo: {empleado['Sueldo']:.2f}\n"
                           f"Renta: {empleado['Renta']:.2f}\n"
                           f"Sueldo Neto: {empleado['Sueldo Neto']:.2f}\n")
                self.result_output.append(resumen)
            

            self.nombre_input.clear()
            self.sueldo_input.clear()

        except ValueError:
            self.result_output.append("Error: Sueldo inválido\n")

    def calcularrenta(self, sueldo):
        return sueldo * 0.30
    
app = QApplication(sys.argv)
window = EmployeeApp()
window.show()
sys.exit(app.exec())
