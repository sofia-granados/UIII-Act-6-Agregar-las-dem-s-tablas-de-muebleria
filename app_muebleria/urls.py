from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # URLs para Empleados
    path('empleados/', views.inicio_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/', views.actualizar_empleados, name='actualizar_empleados'),
    path('empleados/actualizar/<int:id_empleado>/', views.realizar_actualizacion_empleados, name='realizar_actualizacion'),
    path('empleados/borrar/<int:id_empleado>/', views.borrar_empleados, name='borrar_empleado'),
    
    # URLs para Sucursal
    path('sucursal/', views.inicio_sucursal, name='ver_sucursal'),
    path('sucursal/agregar/', views.agregar_sucursal, name='agregar_sucursal'),
    path('sucursal/actualizar/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('sucursal/actualizar/<int:id_sucursal>/', views.realizar_actualizacion_sucursal, name='realizar_actualizacion_sucursal'),
    path('sucursal/borrar/<int:id_sucursal>/', views.borrar_sucursal, name='borrar_sucursal'),
    
    # URLs para Producto
    path('producto/', views.inicio_producto, name='ver_producto'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/actualizar/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/actualizar/<int:id_producto>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:id_producto>/', views.borrar_producto, name='borrar_producto'),
    
    # URLs para Proveedor
    path('proveedor/', views.inicio_proveedor, name='ver_proveedor'),
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/actualizar/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/actualizar/<int:id_proveedor>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:id_proveedor>/', views.borrar_proveedor, name='borrar_proveedor'),
    
    # URLs para Cliente
    path('cliente/', views.inicio_cliente, name='ver_cliente'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/actualizar/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/actualizar/<int:id_cliente>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),
    
    # URLs para Venta
    path('venta/', views.inicio_venta, name='ver_venta'),
    path('venta/agregar/', views.agregar_venta, name='agregar_venta'),
    path('venta/actualizar/', views.actualizar_venta, name='actualizar_venta'),
    path('venta/actualizar/<int:id_venta>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('venta/borrar/<int:id_venta>/', views.borrar_venta, name='borrar_venta'),
    path('venta/detalle/<int:id_venta>/', views.detalle_venta, name='detalle_venta'),
]