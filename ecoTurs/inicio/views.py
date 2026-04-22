from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Recorrido
from .forms import PreInscripcionForm


def principal(request):
    return render(request, "inicio/principal.html")


def proximos(request):
    hoy = timezone.localdate()
    recorridos = Recorrido.objects.filter(fecha__gte=hoy).order_by('fecha')
    return render(request, "inicio/proximos.html", {
        'recorridos': recorridos
    })


def opiniones(request):
    return render(request, "inicio/opiniones.html")


def realizados(request):
    hoy = timezone.localdate()
    recorridos = Recorrido.objects.filter(fecha__lt=hoy).order_by('-fecha')
    return render(request, "inicio/realizados.html", {
        'recorridos': recorridos
    })


def detalles(request, id):
    recorrido = get_object_or_404(Recorrido, id=id)

    if request.method == 'POST':
        form = PreInscripcionForm(request.POST)
        if form.is_valid():
            preinscripcion = form.save(commit=False)
            preinscripcion.recorrido = recorrido
            preinscripcion.save()
            return redirect('Proximos')
    else:
        form = PreInscripcionForm()

    return render(request, "inicio/detalles.html", {
        'recorrido': recorrido,
        'form': form
    })