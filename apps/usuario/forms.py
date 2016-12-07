from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuario(UserCreationForm):
	
	class Meta:
		model = User

		fields=[
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels={
			'username':'Nick',
			'first_name':'Nombre',
			'last_name': 'Apellido',
			'email': 'Correo',
		}