from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):

	TIPO_USUARIO=(
        ('Medico','Medico'),
        ('Paciente','Paciente'),
        ('Especialista','Especialista'),
    )

	Usuario = models.CharField(max_length=20)
	Contraseña = models.CharField(max_length=20)

	TipoUsuario = models.CharField(max_length=500, choices = TIPO_USUARIO, default='Medico')
                                    	
									
class Medico(models.Model):

	Nombre = models.CharField(max_length= 50)
	Apellido = models.CharField(max_length= 50)
	Cedula = models.IntegerField()
	Correo = models.EmailField(blank=True)
	TipoSangre = models.CharField(max_length= 10)
	Telefono = models.CharField(max_length=15)
	Celular = models.CharField(max_length=15)
	FechaNacimiento = models.DateField()

	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)



	def __str__(self):

		return self.Nombre

class GrupoFamiliar(models.Model):

	Nombre = models.CharField(max_length=50)
	Titular = models.CharField(max_length=100)
	IdMedico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Identificador del Medico')

	def __str__(self):

		return self.Nombre


class Paciente(models.Model):

	Nombre = models.CharField(max_length= 50)
	Apellido = models.CharField(max_length= 50)
	Cedula = models.IntegerField()
	Correo = models.EmailField()
	TipoSangre = models.CharField(max_length= 10)
	Telefono = models.CharField(max_length=15)
	Celular = models.CharField(max_length=15)
	FechaNacimiento = models.DateField()
	Estrato = models.IntegerField()
	IdGrupoFamiliar = models.ForeignKey(GrupoFamiliar, on_delete=models.CASCADE, verbose_name='Identificador del GrupoFamiliar')
	

	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)

	def __str__(self):

		return self.Nombre



class Registro(models.Model):

	Sintomas = models.CharField(max_length= 500)
	Medicamentos = models.CharField(max_length= 500)
	SignosVitales = models.CharField(max_length= 500)
	Generacion = models.CharField(max_length= 500)
	Incapacitaciones = models.CharField(max_length= 500, null=True)
	Remisiones = models.CharField(max_length= 500, null=True)
	OrdenesMedicas = models.CharField(max_length= 500)

	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)



	def __str__(self):

		return self.Sintomas


class Laboratorio(models.Model):

	Nombre = models.CharField(max_length= 120)
	Sede = models.CharField(max_length= 500)
	Direccion = models.CharField(max_length= 500)
	Horario = models.CharField(max_length= 120)

	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)



	def __str__(self):

		return self.Nombre


class Cita(models.Model):

	
	IdPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Identificador del Paciente')
	IdMedico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Identificador del Medico')
	IdRegistro = models.ForeignKey(Registro, on_delete=models.CASCADE, verbose_name='Identificador del Registro', blank=True)
	FechaCita = models.DateField()
	TipoCita = models.CharField(max_length= 100, blank=True)
	Observaciones = models.CharField(max_length= 500)

	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)


class Especialista(models.Model):

	Nombre = models.CharField(max_length= 50)
	Apellido = models.CharField(max_length= 50)
	Cedula = models.IntegerField()
	Correo = models.EmailField(blank=True)
	TipoSangre = models.CharField(max_length= 10)
	Telefono = models.CharField(max_length=15)
	Celular = models.CharField(max_length=15)
	FechaNacimiento = models.DateField()
	Especialidad = models.CharField(max_length=50)

	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)




	def __str__(self):

		return self.Nombre

class Examen(models.Model):

	Resultados = models.CharField(max_length=500)
	FechaExamen = models.DateField()
	IdLaboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, verbose_name='Identificador del Laboratorio')
	IdPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Identificador del Paciente')

	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)

class HistoriaClinica(models.Model):

	IdPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Identificador del Paciente')
	IdCita = models.ForeignKey(Cita, on_delete=models.CASCADE, verbose_name='Identificador de la Cita')
	IdExamen = models.ForeignKey(Examen, on_delete=models.CASCADE, verbose_name='Identificador del Examen')


	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)


class CitaEspecialista(models.Model):

	FechaCita = models.DateField()
	TipoCita = models.CharField(max_length= 100)
	Observaciones = models.CharField(max_length= 500)
	IdPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Identificador del Paciente')
	IdEspecialista = models.ForeignKey(Especialista, on_delete=models.CASCADE, verbose_name='Identificador del Especialista')
	IdRegistro = models.ForeignKey(Registro, on_delete=models.CASCADE, verbose_name='Identificador del Registro', blank=True)



	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)



