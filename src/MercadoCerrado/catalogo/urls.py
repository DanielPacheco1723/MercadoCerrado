from django.urls import include, path, re_path
from .views import DetalleProductos, ListaProductos, AgregarProducto, EditarProducto, EliminarProducto
from accounts.views import login_view,logout_view,register_view

urlpatterns = [
    path ('', ListaProductos.as_view(), name = 'catalogo'),
    path ('producto/<int:pk>', DetalleProductos.as_view(), name = 'descripcion_producto'),
    path ('agregar-producto/', AgregarProducto.as_view(), name = 'form-producto'),
    path ('editar-producto/<int:pk>', EditarProducto.as_view(), name = 'editar_producto'),
    path ('eliminar-producto/<int:pk>', EliminarProducto.as_view(), name = 'eliminar_producto'),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view)
]