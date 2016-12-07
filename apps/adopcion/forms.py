from django import forms

from apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields=[
			'nombre',
			'apellido',
			'edad',
			'telefono',
			'email',
			'direccion',
		]
		labels={
			'nombre':'Nombre',
			'apellido':'Apellido',
			'edad':'Edad',
			'telefono':'Telefono (+569 )',
			'email':'Email',
			'direccion':'Direccion',
		}
		widgets={
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellido':forms.TextInput(attrs={'class':'form-control'}),
			'edad':forms.TextInput(attrs={'class':'form-control'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
		}

class SolicitudForm(forms.ModelForm):
	class Meta:
		model = Solicitud
		fields=[
			'numero_mascotas',
			'razones',
		]
		labels={
			'numero_mascotas':'Numero de mascotas',
			'razones':'Razones para adoptar'
		}
		widgets={
			'numero_mascotas':forms.TextInput(attrs={'class':'form-control'}),
			'razones':forms.Textarea(attrs={'class':'form-control'}),
		}