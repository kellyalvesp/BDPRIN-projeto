from django.contrib import admin
from .models import Especialidade
from .models import Medico
from .models import Consulta

admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Consulta)
