from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.core.mail import send_mail
from django.conf import settings
from aplicacion.forms import Formulario
from aplicacion.models import Paciente



# Create your views here.

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request,username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			return render(request,'login.html',{'error':'Usuario y/o contraseña incorrecto'})
	return render(request,'login.html')

def pag_principal(request):
	return render(request,'base.html')

def logout_view(request):
	logout(request)
	return render(request,'login.html')

'''def registro(request):
	if request.method == 'POST':
		usuario = request.POST['usuario']
		password = request.POST['password']
		password_confirmation = request.POST['password_confirmation']

		if password != password_confirmation:
			return render(request,'registro.html',{'error':'La contraseñas no coinciden'})

		try:
			user = User.objects.create_user(username=usuario, password=password)
		except IntegrityError:
			return render(request,'registro.html',{'error':'El usuario ya existe'})

		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		email = request.POST['email']

		user = User.objects.create_user(username=usuario, password=password, first_name=nombre, last_name=apellido, email=email)
		user.is_admin=False
		user.save()
		return redirect('login')

	return render(request,'registro.html')'''

def recuperar_contraseña(request):
	if request.method == 'POST':
		usuario = request.POST['usuario']
		password_nueva = request.POST['password_nueva']
		user = User.objects.get(username=usuario)
		user.set_password(password_nueva)
		user.save()
		return redirect('login')

	return render(request, 'recuperar.html',{'error':'El usuario no existe'})


def contacto(request):
	if request.method == "POST":
		miFormulario = Formulario(request.POST)

		if miFormulario.is_valid():
			infoForm = miFormulario.cleaned_data
			send_mail(infoForm['asunto'], infoForm['mensaje'] + "   Correo:   " + infoForm['email'], infoForm['email'], [''],)
			return render(request, 'envios.html')

	else:
		miFormulario = Formulario()

	return render(request, "formulario_contacto.html", {"form":miFormulario})

def envios(request):
	return render(request, 'envios.html')


@login_required
def dashboard(request):
	return render(request, 'dashboard.html')

def citas(request):
	return render(request, 'citas.html')

def historial(request):
	return render(request, 'historial_clinico.html')

def examen(request):
	return render(request, 'examen.html')

def paciente(request):

	paciente = Paciente.objects.all()
	return render(request, 'paciente.html', {'paciente': paciente})

	return render(request, 'paciente.html')

def laboratorio(request):
	return render(request, 'laboratorio.html')


