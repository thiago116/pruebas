from django.contrib import admin

from aplicacion.models import Paciente, GrupoFamiliar, Medico, Registro, Laboratorio, Cita, Especialista, Examen, HistoriaClinica, CitaEspecialista, Usuario


admin.site.register(Medico)

admin.site.register(GrupoFamiliar)

admin.site.register(Paciente)

admin.site.register(Registro)

admin.site.register(Laboratorio)

admin.site.register(Cita)

admin.site.register(Especialista)

admin.site.register(Examen)

admin.site.register(HistoriaClinica)

admin.site.register(CitaEspecialista)

admin.site.register(Usuario)


# Register your models here.



