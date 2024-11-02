class RegistroMedicacion:
    def __init__(self, fecha, hora, paciente, medicamento, detalle):
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.medicamento = medicamento
        self.detalle = detalle

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente} - Medicacion: {self.medicamento} - {self.detalle}"