from django.urls import path
from agenda.views import *

urlpatterns = [
    path("", view_index, name="inicio"),
    path("agenda/", view_agenda, name="agenda"),
    path("calendario/", view_calendario, name="calendario"),
    path("bitacora/", view_bitacora, name="bitacora"),
]
