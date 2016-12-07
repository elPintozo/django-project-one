from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import RegistroUsuario
# Create your views here.

# Create your views here.
def index(request):
	return render(request,'home/index.html')

class RegistroUsuario(CreateView):
	model = User
	template_name = 'usuario/registrar.html'
	form_class = RegistroUsuario
	success_url = reverse_lazy("mascota:index")
