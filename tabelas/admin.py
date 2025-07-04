from django.contrib import admin
from .models import Especialidade
from .models import Medico
from .models import Consulta
from .models import Paciente
from .models import Receita
from .models import ReceitaMedicamento
from .models import Medicamento

admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Consulta)
admin.site.register(Paciente)
admin.site.register(Receita)
admin.site.register(ReceitaMedicamento)
admin.site.register(Medicamento)