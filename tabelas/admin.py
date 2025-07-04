from django.contrib import admin
from .models import Especialidade
from .models import Medico
from .models import Consulta
from .models import Receitas

admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Consulta)
admin.site.register(Receitas)