from django.contrib import admin
from .models import Proveedor, Cliente, Empleado, Sucursal, Producto, Venta, DetalleVenta

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre', 'telefono', 'correo', 'tipo_producto')
    search_fields = ('nombre', 'correo', 'tipo_producto')
    list_filter = ('tipo_producto',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'telefono', 'correo', 'rfc')
    search_fields = ('nombre', 'correo', 'rfc')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre', 'cargo', 'sueldo', 'fecha_contratacion')
    list_filter = ('cargo',)
    search_fields = ('nombre',)

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('id_sucursal', 'num_sucursal', 'ciudad', 'encargado', 'telefono')
    list_filter = ('ciudad',)
    search_fields = ('ciudad', 'encargado')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'categoria', 'material', 'precio', 'stock')
    list_filter = ('categoria', 'material')
    search_fields = ('nombre',)

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'fecha_venta', 'id_cliente', 'id_empleado', 'total')
    list_filter = ('fecha_venta',)
    search_fields = ('id_cliente__nombre', 'id_empleado__nombre')
    inlines = [DetalleVentaInline]