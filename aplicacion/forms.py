from django import forms

class Formulario(forms.Form):

	asunto = forms.CharField()
	email = forms.CharField()
	mensaje = forms.CharField()