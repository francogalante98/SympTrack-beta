import json
from src.model.entities import Paciente, RegistroSintoma, RegistroMedicacion

class DataManager:
    def __init__(self):
        self.pacientes = []
        self.sintomas = []
        self.medicacion = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agregar_sintoma(self, sintoma):
        self.sintomas.append(sintoma)

    def agregar_medicacion(self, medicacion):
        self.medicacion.append(medicacion)

    def obtener_sintomas_por_paciente(self, nombre_paciente):
        return [s for s in self.sintomas if s.paciente == nombre_paciente]

    def obtener_medicacion_por_paciente(self, nombre_paciente):
        return [m for m in self.medicacion if m.paciente == nombre_paciente]

    def guardar_datos(self):
        datos = {
            "pacientes": [p.nombre for p in self.pacientes],
            "sintomas": [
                {
                    "fecha": s.fecha,
                    "hora": s.hora,
                    "paciente": s.paciente,
                    "sintoma": s.sintoma,
                    "detalle": s.detalle
                } for s in self.sintomas
            ],
            "medicacion": [
                {
                    "fecha": m.fecha,
                    "hora": m.hora,
                    "paciente": m.paciente,
                    "medicamento": m.medicamento,
                    "detalle": m.detalle
                } for m in self.medicacion
            ]
        }
        with open("datos.json", "w") as f:
            json.dump(datos, f)

    def cargar_datos(self):
        try:
            with open("datos.json", "r") as f:
                datos = json.load(f)
            self.pacientes = [Paciente(nombre) for nombre in datos["pacientes"]]
            self.sintomas = [RegistroSintoma(**s) for s in datos["sintomas"]]
            self.medicacion = [RegistroMedicacion(**m) for m in datos["medicacion"]]
        except FileNotFoundError:
            pass
