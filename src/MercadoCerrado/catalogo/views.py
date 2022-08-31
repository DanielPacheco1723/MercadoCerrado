from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.decorators import login_required
from django.forms import NullBooleanField
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from .models import Producto

from django.shortcuts import render, redirect



class ListaProductos (ListView):
    model = Producto
    context_object_name = "catalogo"
    template_name = "catalogo.html"

class DetalleProductos (DetailView):
    model = Producto
    context_object_name = "producto"
    template_name = "productos.html"

class AgregarProducto (CreateView):
    model = Producto
    template_name = "edicion_producto.html"
    fields = ["nombre", "precio", "descripcion", "imagen"]
    success_url = reverse_lazy("catalogo")

class EditarProducto (UpdateView):
    model = Producto
    template_name = "edicion_producto.html"
    fields = ["nombre", "precio", "descripcion", "imagen"]
    success_url = reverse_lazy("catalogo")

class EliminarProducto (DeleteView):
    model = Producto
    template_name = "eliminar_producto.html"
    context_object_name = "producto"
    success_url = reverse_lazy("catalogo")