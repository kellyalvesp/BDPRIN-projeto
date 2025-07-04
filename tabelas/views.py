from rest_framework.viewsets import ModelViewSet
from .models import Especialidade
from .models import Medico
from .models import Consulta
from .models import Paciente
from .models import Receita
from .models import ReceitaMedicamento
from .models import Medicamento
from .serializers import EspecialidadeSerializer
from .serializers import MedicoSerializer
from .serializers import ConsultaSerializer
from .serializers import PacienteSerializer
from .serializers import ReceitaSerializer
from .serializers import ReceitaMedicamentoSerializer
from .serializers import MedicamentoSerializer

class EspecialidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ReceitaViewSet(ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class ReceitaMedicamentoViewSet(ModelViewSet):
    queryset = ReceitaMedicamento.objects.all()
    serializer_class = ReceitaMedicamentoSerializer

class MedicamentoViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer