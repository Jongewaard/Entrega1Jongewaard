from django.shortcuts import render
from agenda.models import *

# Create your views here.
def view_index(request):

    return render(request, "agenda/index.html")

def view_agenda(request):
    consulta_agenda = agenda.objects.all()

    if "guardando" in request.GET:
        existe = False

        if not existe:
            persona = agenda(
                apynombre = request.GET.get('apellido_nombre'),
                f_nac=request.GET.get('fec_nac'),
                e_mail=request.GET.get('e_mail'),
                )
            persona.save()
        else:
            print(f"existe la persona")
        pass
    if 'id_borrar' in request.GET:
        agenda.objects.filter(id=int(request.GET['id_borrar'])).delete()
        pass
    if 'buscando' in request.GET:
        consulta_agenda = agenda.objects.filter(apynombre__icontains = request.GET.get('apellido_nombre'))
        pass

    contexto = {"tabla_sql":consulta_agenda}
    return render(request, "agenda/agenda.html", contexto)


def view_calendario(request):
    '''
    nombre_evento = models.CharField(max_length=100, default="evento")
    f_evento = models.DateTimeField(default=datetime.datetime.now())
    f_aviso_evento = models.DateTimeField(default=datetime.datetime.now())
    '''

    consulta_calendario = calendario.objects.all()

    if "guardando" in request.GET:
        existe = False

        if not existe:
            _evento = calendario(
                nombre_evento = request.GET.get('nombre_evento'),
                f_evento=request.GET.get('f_evento'),
                f_aviso_evento=request.GET.get('f_aviso'),
                )
            _evento.save()
        else:
            print(f"existe el evento")
        pass
    if 'id_borrar' in request.GET:
        calendario.objects.filter(id=int(request.GET['id_borrar'])).delete()
        pass
    if 'buscando' in request.GET:
        consulta_calendario = calendario.objects.filter(nombre_evento__icontains = request.GET.get('evento_a_buscar'))
        pass

    contexto = {"tabla_sql":consulta_calendario}
    return render(request, "agenda/calendario.html",contexto)


def view_bitacora(request):

    return render(request, "agenda/bitacora.html")




