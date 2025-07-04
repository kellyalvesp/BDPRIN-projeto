from django.contrib import admin
from .models import Especialidade
from .models import Medico
from .models import Consulta
from .models import Receita
from .models import ReceitaMedicamento

admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Consulta)
admin.site.register(Receita)
admin.site.register(ReceitaMedicamento)