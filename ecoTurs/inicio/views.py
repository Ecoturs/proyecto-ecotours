from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.utils import timezone
from .models import Recorrido, PreInscripcion, Opinion
from .forms import PreInscripcionForm, RegistroForm, OpinionForm


def principal(request):
    return render(request, "inicio/principal.html")


def proximos(request):
    hoy = timezone.localdate()
    recorridos = Recorrido.objects.filter(fecha__gte=hoy).order_by('fecha')
    return render(request, "inicio/proximos.html", {
        'recorridos': recorridos
    })


def opiniones(request):
    todas = Opinion.objects.all().order_by('-created')
    form = None
    if request.user.is_authenticated:
        recorridos_usuario = Recorrido.objects.filter(
            preinscripcion__usuario=request.user,
            fecha__lt=timezone.localdate()
        ).distinct()
        if request.method == 'POST':
            form = OpinionForm(request.POST)
            if form.is_valid():
                opinion = form.save(commit=False)
                opinion.usuario = request.user
                opinion.save()
                messages.success(request, "¡Opinión agregada correctamente!")
                return redirect('Opiniones')
        else:
            form = OpinionForm()
        form.fields['recorrido'].queryset = recorridos_usuario
    return render(request, "inicio/opiniones.html", {
        'opiniones': todas,
        'form': form
    })


@login_required(login_url='login')
def realizados(request):
    hoy = timezone.localdate()
    preinscripciones = PreInscripcion.objects.filter(
        usuario=request.user,
        recorrido__fecha__lt=hoy
    ).select_related('recorrido')
    recorridos = [p.recorrido for p in preinscripciones]
    return render(request, "inicio/realizados.html", {
        'recorridos': recorridos
    })


def detalles(request, id):
    recorrido = get_object_or_404(Recorrido, id=id)

    if not request.user.is_authenticated:
        return redirect(f'/login/?next=/detalles/{id}/')

    if request.method == 'POST':
        form = PreInscripcionForm(request.POST)
        if form.is_valid():
            preinscripcion = form.save(commit=False)
            preinscripcion.recorrido = recorrido
            preinscripcion.usuario = request.user
            preinscripcion.save()
            messages.success(request, "¡Preinscripción realizada correctamente!")
            return redirect('Proximos')
    else:
        form = PreInscripcionForm()

    return render(request, "inicio/detalles.html", {
        'recorrido': recorrido,
        'form': form
    })


def registro_view(request):
    if request.user.is_authenticated:
        return redirect('Principal')
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"¡Bienvenido {user.username}!")
            return redirect('Principal')
    else:
        form = RegistroForm()
    return render(request, "inicio/registro.html", {'form': form})