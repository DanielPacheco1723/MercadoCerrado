from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
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

def editar_perfil(request):
    print('method:',request.method)
    print('method:',request.POST)
    usuario = request.user
    
    if request.method == 'POST':
        miFormulario = UserChangeForm(request.POST, instance=request.user)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            
            usuario.first_name = data["first_name"]            
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.save()
        return render(request, "base.html", {"mensaje": "Datos actualizados"})
    else:
        miFormulario = UserChangeForm(instance=request.user) 
    return render(request, "editarperfil.html",{"miFormulario": miFormulario})       