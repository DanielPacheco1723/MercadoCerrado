from django.urls import path
from .views import DetalleProductos, ListaProductos, AgregarProducto, EditarProducto, EliminarProducto
from django.contrib.auth.views import LogoutView
from catalogo import views
urlpatterns = [
    path ('', ListaProductos.as_view(), name = 'catalogo'),
    path ('producto/<int:pk>', DetalleProductos.as_view(), name = 'descripcion_producto'),
    path ('agregar-producto/', AgregarProducto.as_view(), name = 'form-producto'),
    path ('editar-producto/<int:pk>', EditarProducto.as_view(), name = 'editar_producto'),
    path ('eliminar-producto/<int:pk>', EliminarProducto.as_view(), name = 'eliminar_producto'),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='MCD1/logout.html'), name="logout"),

]