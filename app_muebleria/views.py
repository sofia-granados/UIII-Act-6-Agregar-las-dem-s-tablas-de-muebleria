from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Sucursal, Producto

# Vistas para Empleados
def inicio_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        empleado = Empleado(
            fecha_contratacion=request.POST['fecha_contratacion'],
            nombre=request.POST['nombre'],
            edad=request.POST['edad'],
            cargo=request.POST['cargo'],
            telefono=request.POST['telefono'],
            sueldo=request.POST['sueldo']
        )
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/agregar_empleado.html')

def actualizar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/actualizar_empleado.html', {'empleados': empleados})

def realizar_actualizacion_empleados(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.nombre = request.POST['nombre']
        empleado.edad = request.POST['edad']
        empleado.cargo = request.POST['cargo']
        empleado.telefono = request.POST['telefono']
        empleado.sueldo = request.POST['sueldo']
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleados(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

def detalle_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    sucursales = empleado.sucursales.all()  # Obtener sucursales donde trabaja
    return render(request, 'empleado/detalle_empleado.html', {
        'empleado': empleado,
        'sucursales': sucursales
    })
# Vistas para Sucursal
def inicio_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursal.html', {'sucursales': sucursales})

def agregar_sucursal(request):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id_empleado=request.POST['id_empleado'])
        sucursal = Sucursal(
            telefono=request.POST['telefono'],
            direccion=request.POST['direccion'],
            num_sucursal=request.POST['num_sucursal'],
            encargado=request.POST['encargado'],
            codigo_postal=request.POST['codigo_postal'],
            ciudad=request.POST['ciudad'],
            id_empleado=empleado
        )
        sucursal.save()
        return redirect('ver_sucursal')
    
    empleados = Empleado.objects.all()
    return render(request, 'sucursal/agregar_sucursal.html', {'empleados': empleados})

def actualizar_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursales': sucursales})

def realizar_actualizacion_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id_empleado=request.POST['id_empleado'])
        sucursal.telefono = request.POST['telefono']
        sucursal.direccion = request.POST['direccion']
        sucursal.num_sucursal = request.POST['num_sucursal']
        sucursal.encargado = request.POST['encargado']
        sucursal.codigo_postal = request.POST['codigo_postal']
        sucursal.ciudad = request.POST['ciudad']
        sucursal.id_empleado = empleado
        sucursal.save()
        return redirect('ver_sucursal')
    
    empleados = Empleado.objects.all()
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal, 'empleados': empleados})

def borrar_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('ver_sucursal')
    return render(request, 'sucursal/borrar_sucursal.html', {'sucursal': sucursal})

def detalle_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    productos = sucursal.productos.all()  # Productos disponibles en la sucursal
    return render(request, 'sucursal/detalle_sucursal.html', {
        'sucursal': sucursal,
        'productos': productos
    })
# Vistas para Producto
def inicio_producto(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_producto.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        # Crear producto
        producto = Producto(
            nombre=request.POST['nombre'],
            categoria=request.POST['categoria'],
            material=request.POST['material'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            color=request.POST['color']
        )
        producto.save()
        
        # Agregar relaciones ManyToMany con sucursales
        sucursales_ids = request.POST.getlist('sucursales')
        for sucursal_id in sucursales_ids:
            sucursal = get_object_or_404(Sucursal, id_sucursal=sucursal_id)
            producto.sucursales.add(sucursal)
        
        return redirect('ver_producto')
    
    sucursales = Sucursal.objects.all()
    return render(request, 'producto/agregar_producto.html', {'sucursales': sucursales})

def actualizar_producto(request):
    productos = Producto.objects.all()
    return render(request, 'producto/actualizar_producto.html', {'productos': productos})

def realizar_actualizacion_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.categoria = request.POST['categoria']
        producto.material = request.POST['material']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.color = request.POST['color']
        producto.save()
        
        # Actualizar relaciones ManyToMany
        producto.sucursales.clear()
        sucursales_ids = request.POST.getlist('sucursales')
        for sucursal_id in sucursales_ids:
            sucursal = get_object_or_404(Sucursal, id_sucursal=sucursal_id)
            producto.sucursales.add(sucursal)
        
        return redirect('ver_producto')
    
    sucursales = Sucursal.objects.all()
    producto_sucursales = producto.sucursales.all()
    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto, 
        'sucursales': sucursales,
        'producto_sucursales': producto_sucursales
    })

def borrar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

def detalle_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    sucursales = producto.sucursales.all()  # Sucursales donde está disponible
    return render(request, 'producto/detalle_producto.html', {
        'producto': producto,
        'sucursales': sucursales
    })
# Vista de inicio
def inicio(request):
    # Estadísticas para mostrar en el inicio
    total_empleados = Empleado.objects.count()
    total_sucursales = Sucursal.objects.count()
    total_productos = Producto.objects.count()
    
    return render(request, 'inicio.html', {
        'total_empleados': total_empleados,
        'total_sucursales': total_sucursales,
        'total_productos': total_productos
    })

from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Sucursal, Producto, Proveedor, Cliente, Venta, DetalleVenta
from django.db.models import Sum
from django.utils import timezone

# Vistas para Proveedor
def inicio_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        proveedor = Proveedor(
            nombre=request.POST['nombre'],
            telefono=request.POST['telefono'],
            correo=request.POST['correo'],
            direccion=request.POST['direccion'],
            tipo_producto=request.POST['tipo_producto']
        )
        proveedor.save()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/agregar_proveedor.html')

def actualizar_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedores': proveedores})

def realizar_actualizacion_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id_proveedor)
    
    if request.method == 'POST':
        proveedor.nombre = request.POST['nombre']
        proveedor.telefono = request.POST['telefono']
        proveedor.correo = request.POST['correo']
        proveedor.direccion = request.POST['direccion']
        proveedor.tipo_producto = request.POST['tipo_producto']
        proveedor.save()
        return redirect('ver_proveedor')
    
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def borrar_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id_proveedor)
    
    # Verificar si tiene productos asociados
    tiene_productos = proveedor.productos.exists()
    
    if request.method == 'POST' and not tiene_productos:
        proveedor.delete()
        return redirect('ver_proveedor')
    
    return render(request, 'proveedor/borrar_proveedor.html', {
        'proveedor': proveedor,
        'tiene_productos': tiene_productos
    })

def detalle_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id_proveedor)
    productos = proveedor.productos.all()  # Productos que suministra
    return render(request, 'proveedor/detalle_proveedor.html', {
        'proveedor': proveedor,
        'productos': productos
    })

# Vistas para Cliente
def inicio_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        cliente = Cliente(
            nombre=request.POST['nombre'],
            telefono=request.POST['telefono'],
            correo=request.POST['correo'],
            direccion=request.POST['direccion'],
            rfc=request.POST['rfc']
        )
        cliente.save()
        return redirect('ver_cliente')
    return render(request, 'cliente/agregar_cliente.html')

def actualizar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/actualizar_cliente.html', {'clientes': clientes})

def realizar_actualizacion_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.telefono = request.POST['telefono']
        cliente.correo = request.POST['correo']
        cliente.direccion = request.POST['direccion']
        cliente.rfc = request.POST['rfc']
        cliente.save()
        return redirect('ver_cliente')
    
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

def detalle_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    ventas = cliente.ventas.all()  # Ventas realizadas por el cliente
    
    # Calcular total gastado manualmente
    total_gastado = 0
    for venta in ventas:
        total_gastado += float(venta.total)  # Convertir Decimal a float para sumar
    
    return render(request, 'cliente/detalle_cliente.html', {
        'cliente': cliente,
        'ventas': ventas,
        'total_gastado': f"{total_gastado:.2f}"  # Formatear a 2 decimales
    })

# Vistas para Venta
def inicio_venta(request):
    ventas = Venta.objects.all().order_by('-fecha_venta')
    return render(request, 'venta/ver_venta.html', {'ventas': ventas})

def agregar_venta(request):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id_cliente=request.POST['id_cliente'])
        empleado = get_object_or_404(Empleado, id_empleado=request.POST['id_empleado'])
        
        venta = Venta(
            id_cliente=cliente,
            id_empleado=empleado
        )
        venta.save()
        
        # Procesar productos de la venta
        productos_ids = request.POST.getlist('productos[]')
        cantidades = request.POST.getlist('cantidades[]')
        total = 0
        
        for producto_id, cantidad in zip(productos_ids, cantidades):
            if producto_id and cantidad:
                producto = get_object_or_404(Producto, id_producto=producto_id)
                subtotal = producto.precio * int(cantidad)
                
                detalle = DetalleVenta(
                    id_venta=venta,
                    id_producto=producto,
                    cantidad=cantidad,
                    subtotal=subtotal
                )
                detalle.save()
                total += subtotal
                
                # Actualizar stock
                producto.stock -= int(cantidad)
                producto.save()
        
        # Actualizar total de la venta
        venta.total = total
        venta.save()
        
        return redirect('ver_venta')
    
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    productos = Producto.objects.filter(stock__gt=0)
    return render(request, 'venta/agregar_venta.html', {
        'clientes': clientes,
        'empleados': empleados,
        'productos': productos
    })

def actualizar_venta(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/actualizar_venta.html', {'ventas': ventas})

def realizar_actualizacion_venta(request, id_venta):
    venta = get_object_or_404(Venta, id_venta=id_venta)
    
    if request.method == 'POST':
        # Actualizar cliente y empleado
        cliente = get_object_or_404(Cliente, id_cliente=request.POST['id_cliente'])
        empleado = get_object_or_404(Empleado, id_empleado=request.POST['id_empleado'])
        
        venta.id_cliente = cliente
        venta.id_empleado = empleado
        
        # Procesar productos actualizados
        detalles_actuales = {d.id_detalle: d for d in venta.detalles.all()}
        productos_ids = request.POST.getlist('productos[]')
        cantidades = request.POST.getlist('cantidades[]')
        detalles_ids = request.POST.getlist('detalles_ids[]')
        
        total = 0
        
        # Actualizar o crear detalles
        for i, (producto_id, cantidad, detalle_id) in enumerate(zip(productos_ids, cantidades, detalles_ids)):
            if producto_id and cantidad and int(cantidad) > 0:
                producto = get_object_or_404(Producto, id_producto=producto_id)
                subtotal = producto.precio * int(cantidad)
                
                if detalle_id and detalle_id != 'new':
                    # Actualizar detalle existente
                    detalle = DetalleVenta.objects.get(id_detalle=detalle_id)
                    # Restaurar stock anterior
                    producto_anterior = detalle.id_producto
                    producto_anterior.stock += detalle.cantidad
                    producto_anterior.save()
                    
                    # Actualizar detalle
                    detalle.id_producto = producto
                    detalle.cantidad = cantidad
                    detalle.subtotal = subtotal
                    detalle.save()
                    
                    # Reducir stock nuevo
                    producto.stock -= int(cantidad)
                    producto.save()
                    
                    # Eliminar de detalles actuales
                    if int(detalle_id) in detalles_actuales:
                        del detalles_actuales[int(detalle_id)]
                else:
                    # Crear nuevo detalle
                    detalle = DetalleVenta(
                        id_venta=venta,
                        id_producto=producto,
                        cantidad=cantidad,
                        subtotal=subtotal
                    )
                    detalle.save()
                    
                    # Reducir stock
                    producto.stock -= int(cantidad)
                    producto.save()
                
                total += subtotal
        
        # Eliminar detalles que ya no están en la venta
        for detalle in detalles_actuales.values():
            # Restaurar stock
            producto = detalle.id_producto
            producto.stock += detalle.cantidad
            producto.save()
            detalle.delete()
        
        # Actualizar total de la venta
        venta.total = total
        venta.save()
        
        return redirect('detalle_venta', id_venta=venta.id_venta)
    
    # Obtener datos para el formulario
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    productos = Producto.objects.all()
    detalles = venta.detalles.all()
    
    return render(request, 'venta/actualizar_venta.html', {
        'venta': venta,
        'clientes': clientes,
        'empleados': empleados,
        'productos': productos,
        'detalles': detalles
    })

def borrar_venta(request, id_venta):
    venta = get_object_or_404(Venta, id_venta=id_venta)
    if request.method == 'POST':
        # Restaurar stock de productos antes de eliminar
        for detalle in venta.detalles.all():
            producto = detalle.id_producto
            producto.stock += detalle.cantidad
            producto.save()
        
        venta.delete()
        return redirect('ver_venta')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})

def detalle_venta(request, id_venta):
    venta = get_object_or_404(Venta, id_venta=id_venta)
    detalles = venta.detalles.all()
    return render(request, 'venta/detalle_venta.html', {'venta': venta, 'detalles': detalles})

# Actualizar vista de inicio con más estadísticas
def inicio(request):
    total_empleados = Empleado.objects.count()
    total_sucursales = Sucursal.objects.count()
    total_productos = Producto.objects.count()
    total_clientes = Cliente.objects.count()
    total_proveedores = Proveedor.objects.count()
    total_ventas = Venta.objects.count()
    ventas_hoy = Venta.objects.filter(fecha_venta__date=timezone.now().date()).count()
    
    # Total de ventas del día
    ventas_hoy_total = Venta.objects.filter(fecha_venta__date=timezone.now().date()).aggregate(
        total=Sum('total')
    )['total'] or 0
    
    return render(request, 'inicio.html', {
        'total_empleados': total_empleados,
        'total_sucursales': total_sucursales,
        'total_productos': total_productos,
        'total_clientes': total_clientes,
        'total_proveedores': total_proveedores,
        'total_ventas': total_ventas,
        'ventas_hoy': ventas_hoy,
        'ventas_hoy_total': ventas_hoy_total
    })

