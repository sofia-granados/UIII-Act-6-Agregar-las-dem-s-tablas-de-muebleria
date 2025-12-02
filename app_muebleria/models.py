from django.db import models

# Choices para los campos
CARGO_CHOICES = [
    ('VENDEDOR', 'Vendedor'),
    ('GERENTE', 'Gerente'),
    ('ALMACEN', 'Almacen'),
    ('CAJERO', 'Cajero'),
]

CATEGORIA_CHOICES = [
    ('SALA', 'Sala'),
    ('COMEDOR', 'Comedor'),
    ('RECAMARA', 'Recámara'),
    ('OFICINA', 'Oficina'),
]

MATERIAL_CHOICES = [
    ('MADERA', 'Madera'),
    ('METAL', 'Metal'),
    ('PLASTICO', 'Plástico'),
    ('VIDRIO', 'Vidrio'),
]

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=200)
    tipo_producto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=200)
    rfc = models.CharField(max_length=13)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Empleado(models.Model):
    fecha_contratacion = models.DateField()
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES)
    telefono = models.CharField(max_length=15)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre} - {self.cargo}"

class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    num_sucursal = models.IntegerField()
    encargado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=50)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="sucursales")
    
    def __str__(self):
        return f"Sucursal {self.num_sucursal} - {self.ciudad}"

class Producto(models.Model):    
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    precio = models.FloatField()
    stock = models.IntegerField()
    color = models.CharField(max_length=30)
    id_producto = models.AutoField(primary_key=True)
    sucursales = models.ManyToManyField(Sucursal, related_name="productos")
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True, related_name="productos")
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ventas")
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="ventas")
    
    def __str__(self):
        return f"Venta {self.id_venta} - {self.fecha_venta.strftime('%Y-%m-%d')}"
    
    class Meta:
        db_table = 'ventas'
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

class DetalleVenta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name="detalles")
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="detalles_venta")
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Detalle {self.id_detalle} - Venta {self.id_venta.id_venta}"
    
    class Meta:
        db_table = 'detalle_ventas'
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"