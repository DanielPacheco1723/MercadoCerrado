from django.urls import path
from .views import DetalleProductos, ListaProductos, AgregarProducto, EditarProducto, EliminarProducto

urlpatterns = [
    path ('', ListaProductos.as_view(), name = 'catalogo'),
    path ('producto/<int:pk>', DetalleProductos.as_view(), name = 'descripcion_producto'),
    path ('agregar-producto/', AgregarProducto.as_view(), name = 'form-producto'),
    path ('editar-producto/<int:pk>', EditarProducto.as_view(), name = 'editar_producto'),
    path ('eliminar-producto/<int:pk>', EliminarProducto.as_view(), name = 'eliminar_producto')


]