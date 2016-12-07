from django.conf.urls import url
from apps.usuario.views import RegistroUsuario, index

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^registrar$', RegistroUsuario.as_view(), name='usuario_crear'),
]
