from django.contrib import admin
from agenda.models import agenda, calendario, bitacora

# Register your models here.
admin.site.register(agenda)
admin.site.register(calendario)
admin.site.register(bitacora)