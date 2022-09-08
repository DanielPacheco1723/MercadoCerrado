from django.urls import include, path, re_path
from .views import DetalleProductos, ListaProductos, AgregarProducto, EditarProducto, EliminarProducto, editar_perfil,about_us
from accounts.views import login_view,logout_view,register_view

urlpatterns = [
    path ('', ListaProductos.as_view(), name = 'catalogo'),
    path ('producto/<int:pk>', DetalleProductos.as_view(), name = 'descripcion_producto'),
    path ('agregar-producto/', AgregarProducto.as_view(), name = 'form-producto'),
    path ('editar-producto/<int:pk>', EditarProducto.as_view(), name = 'editar_producto'),
    path ('eliminar-producto/<int:pk>', EliminarProducto.as_view(), name = 'eliminar_producto'),
    path('accounts/login/', login_view),
    path('accounts/logout/', logout_view),
    path('accounts/singup/', register_view),
    path('accounts/profile/', editar_perfil, name="EditarPerfil"),
    path('about-us/', about_us, name="about_us")
]