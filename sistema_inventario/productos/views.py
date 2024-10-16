from django.shortcuts import render

# data_productos = [
#     {"id": 1, "nombre": "Producto 1", "imagen": "/static/img/productos/producto1.webp"},
#     {"id": 2, "nombre": "Producto 2", "imagen": "/static/img/productos/producto2.jpeg"},
#     {"id": 3, "nombre": "Producto 3", "imagen": "/static/img/productos/producto3.jpeg"},
#     {"id": 4, "nombre": "Producto 4", "imagen": "/static/img/productos/producto4.jpeg"},
# ]

data_productos = [
    {"id": 1, "nombre": "Producto 1", "imagen": "producto1.webp", "descripcion": "producto 1"},
    {"id": 2, "nombre": "Producto 2", "imagen": "producto2.jpeg", "descripcion": "producto 2 producto 2 producto 2 producto 2 "},
    {"id": 3, "nombre": "Producto 3", "imagen": "producto3.jpeg", "descripcion": "producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3 producto 3"},
    {"id": 4, "nombre": "Producto 4", "imagen": "producto4.jpeg", "descripcion": "producto 4 producto 4 producto 4 producto 4 producto 4 producto 4 producto 4 producto 4"},
]
# Create your views here.

def productos(request):
    contexto = {
        "productos": data_productos
    }
    return render(request, 'productos/productos.html', contexto)
