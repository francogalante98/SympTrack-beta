class RegistroSintoma:
    def __init__(self, fecha, hora, paciente, sintoma, detalle):
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.sintoma = sintoma
        self.detalle = detalle

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente} - Sintoma: {self.sintoma} - {self.detalle}"