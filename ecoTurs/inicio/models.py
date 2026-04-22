from django.db import models
from django.contrib.auth.models import User


class Recorrido(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    fecha = models.DateField(verbose_name="Fecha")
    estado = models.CharField(max_length=50, verbose_name="Estado")
    ciudad = models.CharField(max_length=50, verbose_name="Ciudad")
    costo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo")
    imagen = models.ImageField(upload_to="recorridos/", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, default="", verbose_name="Descripción")

    class Meta:
        verbose_name = "Recorrido"
        verbose_name_plural = "Recorridos"
        ordering = ["fecha"]

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"


class PreInscripcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Usuario")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    ciudad = models.CharField(max_length=50, verbose_name="Ciudad")
    estado = models.CharField(max_length=50, verbose_name="Estado")
    recorrido = models.ForeignKey(Recorrido, on_delete=models.CASCADE, verbose_name="Recorrido")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Preinscripción"
        verbose_name_plural = "Preinscripciones"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.nombre} - {self.recorrido.nombre}"


class Opinion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    comentario = models.TextField(verbose_name="Comentario")
    calificacion = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        verbose_name="Calificación"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Opinión"
        verbose_name_plural = "Opiniones"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.usuario.username} - {self.calificacion}★"