from django.shortcuts import render

# data_productos = [
#     {"id": 1, "nombre": "Producto 1", "imagen": "/static/img/productos/producto1.webp"},
#     {"id": 2, "nombre": "Producto 2", "imagen": "/static/img/productos/producto2.jpeg"},
#     {"id": 3, "nombre": "Producto 3", "imagen": "/static/img/productos/producto3.jpeg"},
#     {"id": 4, "nombre": "Producto 4", "imagen": "/static/img/productos/producto4.jpeg"},
# ]

data_productos = [
    {"id": 1, "nombre": "Producto 1", "imagen": "producto1.webp", "descripcion": "Descripción producto 1", "precio": 800, "stock": 50, "descuento": 0},
    {"id": 2, "nombre": "Producto 2", "imagen": "producto2.jpeg", "descripcion": "Descripción producto 2", "precio": 900, "stock": 150, "descuento": 0},
    {"id": 3, "nombre": "Producto 3", "imagen": "producto3.jpeg", "descripcion": "Descripción producto 3", "precio": 1000, "stock": 30, "descuento": 350},
    {"id": 4, "nombre": "Producto 4", "imagen": "producto4.jpeg", "descripcion": "Descripción producto 4", "precio": 850, "stock": 5, "descuento": 0},
]
# Create your views here.

def productos(request):
    
    for producto in data_productos:
        producto["precio_final"] = producto["precio"] - producto["descuento"]

    contexto = {
        "productos": data_productos
    }
    return render(request, 'productos/productos.html', contexto)


def detalle_producto(request, id):
    
    # BUSCAR PRODUCTO POR ID
    
    def buscar_producto(datos, id_a_buscar):
        for producto in datos:
            if producto["id"] == id_a_buscar:
                return producto
        
    producto = buscar_producto(data_productos, id)
    
    contexto = {
        "id": id,
        "producto": producto
    }
    return render(request, 'productos/detalle_producto.html', contexto)

