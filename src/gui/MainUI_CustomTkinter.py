import customtkinter as ctk
from tkcalendar import DateEntry
#from datetime import datetime
from src.model.dao import DataManager
from src.model.entities import Paciente, RegistroSintoma, RegistroMedicacion


# Configuración de CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SympTrack beta")
        self.geometry("800x700")
        self.configure(padx=20, pady=20)
        self.DataManager = DataManager()
        self.DataManager.cargar_datos()

        # Titulo central
        self.title_label = ctk.CTkLabel(self, text="SympTrack β", font=("Arial", 18))
        self.title_label.pack(pady=10)

        # Frame PACIENTES
        self.paciente_frame = ctk.CTkFrame(self)
        self.paciente_frame.pack(pady=20)

        self.fila_frame = ctk.CTkFrame(self.paciente_frame)
        self.fila_frame.pack(anchor="center")

        self.paciente_label = ctk.CTkLabel(self.fila_frame, text="Nuevo Paciente: ingrese Nombre - DNI")
        self.paciente_label.pack(side="left", padx=5)

        self.nombrepaciente_entry = ctk.CTkEntry(self.fila_frame, placeholder_text="Nombre - DNI")
        self.nombrepaciente_entry.pack(side="left", padx=5)

        self.ingresar_button = ctk.CTkButton(self.fila_frame, text="Registrar Paciente", command= self.agregar_paciente)
        self.ingresar_button.pack(side="left", padx=5)

        # Frame izquierdo: Registros
        self.registros_frame = ctk.CTkFrame(self)
        self.registros_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.registros_label = ctk.CTkLabel(self.registros_frame, text="Registros", font=("Arial", 14))
        self.registros_label.pack(pady=5)

        # Subframe para síntomas
        self.sintomas_frame = ctk.CTkFrame(self.registros_frame)
        self.sintomas_frame.pack(fill="x", pady=5)

        self.sintomas_label = ctk.CTkLabel(self.sintomas_frame, text="Síntomas")
        self.sintomas_label.pack(pady=5)

        # Combobox para seleccionar paciente
        self.combo_paciente_sintoma = ctk.CTkComboBox(self.sintomas_frame, values=[p.nombre for p in self.DataManager.pacientes])
        self.combo_paciente_sintoma.pack(fill="x", padx=5, pady=2)
        self.combo_paciente_sintoma.set("Seleccionar paciente")

        # Frame para "Fecha" y "Hora" en una sola fila
        self.fecha_hora_frame = ctk.CTkFrame(self.sintomas_frame)
        self.fecha_hora_frame.pack(pady=5)

        self.fecha_label = ctk.CTkLabel(self.fecha_hora_frame, text="Fecha y hora Sintomas  ")
        self.fecha_label.pack(side="left", padx=(5, 5))
        self.fecha_entry_sintomas = DateEntry(self.fecha_hora_frame, width=14, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry_sintomas.pack(side="left", padx=(0, 10))

        self.hour_entry_sintomas = ctk.CTkEntry(self.fecha_hora_frame, width=30, placeholder_text="HH")
        self.hour_entry_sintomas.pack(side="left", padx=(0, 5))
        self.minute_entry_sintomas = ctk.CTkEntry(self.fecha_hora_frame, width=30, placeholder_text="MM")
        self.minute_entry_sintomas.pack(side="left", padx=(0, 5))

        self.sintoma_entry = ctk.CTkEntry(self.sintomas_frame, placeholder_text="Síntoma")
        self.sintoma_entry.pack(fill="x", padx=5, pady=2)
        self.descripcion_entry_sintomas = ctk.CTkEntry(self.sintomas_frame, placeholder_text="Descripción")
        self.descripcion_entry_sintomas.pack(fill="x", padx=5, pady=2)

        self.ingresar_sintomas_button = ctk.CTkButton(self.sintomas_frame, text="Registrar Síntoma", command=self.nuevo_sintoma)
        self.ingresar_sintomas_button.pack(pady=5)

        # Subframe para medicación
        self.medicacion_frame = ctk.CTkFrame(self.registros_frame)
        self.medicacion_frame.pack(fill="x", pady=5)

        self.medicacion_label = ctk.CTkLabel(self.medicacion_frame, text="Medicación")
        self.medicacion_label.pack(pady=5)  # Centrado

        self.combo_paciente_medicacion = ctk.CTkComboBox(self.medicacion_frame, values=[p.nombre for p in self.DataManager.pacientes])
        self.combo_paciente_medicacion.pack(fill="x", padx=5, pady=2)
        self.combo_paciente_medicacion.set("Seleccionar paciente")

        self.fecha_hora_frame_medicacion = ctk.CTkFrame(self.medicacion_frame)
        self.fecha_hora_frame_medicacion.pack(pady=5)
        self.fecha_label_medicacion = ctk.CTkLabel(self.fecha_hora_frame_medicacion, text="Fecha")
        self.fecha_label_medicacion.pack(side="left", padx=(5, 5))
        self.fecha_entry_medicacion = DateEntry(self.fecha_hora_frame_medicacion, width=14, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry_medicacion.pack(side="left", padx=(0, 10))

        self.hour_entry_medicacion = ctk.CTkEntry(self.fecha_hora_frame_medicacion, width=30, placeholder_text="HH")
        self.hour_entry_medicacion.pack(side="left", padx=(0, 5))
        self.minute_entry_medicacion = ctk.CTkEntry(self.fecha_hora_frame_medicacion, width=30, placeholder_text="MM")
        self.minute_entry_medicacion.pack(side="left", padx=(0, 5))

        self.medicamento_entry = ctk.CTkEntry(self.medicacion_frame, placeholder_text="Medicamento")
        self.medicamento_entry.pack(fill="x", padx=5, pady=2)

        self.descripcion_entry_medicacion = ctk.CTkEntry(self.medicacion_frame, placeholder_text="Descripción")
        self.descripcion_entry_medicacion.pack(fill="x", padx=5, pady=2)

        self.ingresar_medicacion_button = ctk.CTkButton(self.medicacion_frame, text="Registrar Medicación", command=self.nueva_medicacion)
        self.ingresar_medicacion_button.pack(pady=5)

        # Frame derecho: Reportes
        self.reportes_frame = ctk.CTkFrame(self)
        self.reportes_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.reportes_label = ctk.CTkLabel(self.reportes_frame, text="Reportes", font=("Arial", 14))
        self.reportes_label.pack(pady=5)
        self.combo_paciente_registro = ctk.CTkComboBox(self.reportes_frame, values=[p.nombre for p in self.DataManager.pacientes])
        self.combo_paciente_registro.pack(fill="x", padx=5, pady=2)
        self.combo_paciente_registro.set("Seleccionar paciente")
        self.ver_informes_button = ctk.CTkButton(self.reportes_frame, text="Ver Informes", command=self.mostrar_registros)  #AGREGAR COMANDO
        self.ver_informes_button.pack(pady=5)

        # Text box para mostrar los reportes
        self.ver_informes = ctk.CTkTextbox(self.reportes_frame, width=400, height=300)
        self.ver_informes.pack(fill="both", expand=True, padx=5, pady=5)

    def agregar_paciente(self):
        nombrepaciente = self.nombrepaciente_entry.get()
        if nombrepaciente:
            paciente = Paciente(nombrepaciente)
            self.DataManager.agregar_paciente(paciente)
            self.nombrepaciente_entry.delete(0, ctk.END)
            self.actualizar_combos_pacientes()
            self.DataManager.guardar_datos()


    def actualizar_combos_pacientes(self):
        pacientes = [p.nombre for p in self.DataManager.pacientes]
        self.combo_paciente_sintoma.configure(values=pacientes)
        self.combo_paciente_medicacion.configure(values=pacientes)
        self.combo_paciente_registro.configure(values=pacientes)

    def nuevo_sintoma(self):
        paciente = self.combo_paciente_sintoma.get()
        fecha = self.fecha_entry_sintomas.get_date().strftime("%Y-%m-%d")
        hora = f"{self.hour_entry_sintomas.get()}:{self.minute_entry_sintomas.get()}"
        sintoma = self.sintoma_entry.get()
        detalle = self.descripcion_entry_sintomas.get()
        if paciente and sintoma:
            nuevo_sintoma = RegistroSintoma(fecha, hora, paciente, sintoma, detalle)
            self.DataManager.agregar_sintoma(nuevo_sintoma)
            self.combo_paciente_sintoma.set("Seleccionar paciente")
            self.sintoma_entry.delete(0, ctk.END)
            self.descripcion_entry_sintomas.delete(0, ctk.END)
            self.DataManager.guardar_datos()


    def nueva_medicacion(self):
        paciente = self.combo_paciente_medicacion.get()
        fecha = self.fecha_entry_medicacion.get_date().strftime("%Y-%m-%d")
        hora = f"{self.hour_entry_medicacion.get()}:{self.minute_entry_medicacion.get()}"
        medicameto = self.medicamento_entry.get()
        detalle = self.descripcion_entry_medicacion.get()
        if paciente and medicameto:
            nuevo_sintoma = RegistroMedicacion(fecha, hora, paciente, medicameto, detalle)
            self.DataManager.agregar_medicacion(nuevo_sintoma)
            self.combo_paciente_medicacion.set("Seleccionar paciente")
            self.medicamento_entry.delete(0, ctk.END)
            self.descripcion_entry_medicacion.delete(0, ctk.END)
            self.DataManager.guardar_datos()


    def mostrar_registros(self):
        paciente = self.combo_paciente_registro.get()
        if paciente:
            sintomas = self.DataManager.obtener_sintomas_por_paciente(paciente)
            medicacion = self.DataManager.obtener_medicacion_por_paciente(paciente)

            self.ver_informes.delete('1.0', ctk.END)
            self.ver_informes.insert(ctk.END, f"Registros para {paciente}:\n\n")
            self.ver_informes.insert(ctk.END, "Síntomas:\n")
            for sintoma in sintomas:
                self.ver_informes.insert(ctk.END,   f"{str(sintoma)}\n")
            self.ver_informes.insert(ctk.END, "\nMedicación:\n")
            for medicamento in medicacion:
                self.ver_informes.insert(ctk.END, f"{str(medicamento)}\n")









#FALLAS A MIRAR EN CLASE
#FUNCIONALIDAD BOTONES AL CREAR PACIENTE Y AGREGAR REGISTRO
#ERROR DE APERTURA AL TENER COMMAND EL BOTON DE VER INFORMES