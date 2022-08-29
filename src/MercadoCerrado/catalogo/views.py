from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms import NullBooleanField
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from .models import Producto
from .forms import UserRegisterForm

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

def register(request):
      form = UserRegisterForm(request.POST)
      if form.is_valid():
            username = form.cleaned_data['username']
            first_name=form.cleaned_data['first_name']
            form.save()
            return render(request, "index.html", {"mensaje":"Usuario Creado!"})
      else:
            form = UserRegisterForm()
      return render(request, "registro.html", {"form": form})    

def login_request(request):
      
      
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  
                  user = authenticate(username=usuario, password = contra)
                  
                  
                  if user is not None:
                        login(request, user)
                        avatares = Avatar.objects.filter(user=request.user.id).exists()
                        if avatares == True:
                              avatares = Avatar.objects.filter(user=request.user.id)
                              print(avatares)
                              return render(request, "base.html", {"url": avatares[0].imagen.url})
                        #return render(request, "/base.html", {"mensaje": f"Bienvenido {usuario}"})
                        else:
                              return render(request, "/base.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        return render(request, "error.html", {"mensaje": f"Error, datos incorrectos"})
            
            else:
                  return render(request,"/error.html", {"mensaje": f"Error, formulario equivocado"})      
      
      form = AuthenticationForm()
      return render(request, "login.html", {"form": form})        
      
      
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  
                  user = authenticate(username=usuario, password = contra)
                  
                  if user is not None:
                        login(request, user)
                        avatares = Avatar.objects.filter(user=request.user.id)
                        return render(request, "/base.html", {"url": avatares[0].imagen.url})
                        #return render(request, "/base.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        return render(request, "/error.html", {"mensaje": f"Error, datos incorrectos"})
            
            else:
                  return render(request,"/error.html", {"mensaje": f"Error, formulario equivocado"})      
      
      form = AuthenticationForm()
      return render(request, "/login.html", {"form": form})   