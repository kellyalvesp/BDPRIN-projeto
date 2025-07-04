from rest_framework.serializers import ModelSerializer
from .models import Especialidade
from .models import Medico
from .models import Consulta
from .models import Paciente
from .models import Receita
from .models import ReceitaMedicamento
from .models import Medicamento

class EspecialidadeSerializer(ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'

class MedicoSerializer(ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class ConsultaSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente 
        fields = '__all__'

class ReceitaSerializer(ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'

class ReceitaMedicamentoSerializer(ModelSerializer):
    class Meta:
        model = ReceitaMedicamento
        fields = '__all__'

class MedicamentoSerializer(ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'