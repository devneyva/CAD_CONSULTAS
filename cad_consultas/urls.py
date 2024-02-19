from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index , cadrastro, deletar
from rest_framework import routers
from .api.viewsets import ConsultaViewSet

router = routers.DefaultRouter()
router.register('cad_consultas', ConsultaViewSet)


urlpatterns = [
    path('', index , name = 'index'),
    path('cadastro/', cadrastro, name='cadastro'),
    path('deletar/<int:id>', deletar, name= 'deletar'),
    path('api_consultas/', include (router.urls)),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)