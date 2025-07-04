from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tabelas.views import EspecialidadeViewSet
from tabelas.views import MedicoViewSet
from tabelas.views import ConsultaViewSet
from tabelas.views import PacienteViewSet
from tabelas.views import ReceitaViewSet
from tabelas.views import ReceitaMedicamentoViewSet
from tabelas.views import MedicamentoViewSet

router = DefaultRouter()
router.register(r'especialidade', EspecialidadeViewSet)
router.register(r'medico', MedicoViewSet)
router.register(r'consulta', ConsultaViewSet)
router.register(r'paciente', PacienteViewSet)
router.register(r'receita', ReceitaViewSet)
router.register(r'receitamedicamento', ReceitaMedicamentoViewSet)
router.register(r'medicamento', MedicamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]