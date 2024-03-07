from django.shortcuts import render
from .models import Category, Product

def index(request):
    # Obtener todas las categorías y productos
    categorias = Category.objects.all()
    productos = Product.objects.all()

    # Pasar las categorías y productos al contexto para usarlos en la plantilla
    context = {
        'categories': categorias,
        'products': productos,
    }

    # Renderizar la plantilla 'index.html' con el contexto
    return render(request, 'shop/index.html', context)


def product_detail(request,pk):
    # Obtener todas las categorías y productos
    product = Product.objects.get(id=pk)
    context = {
        'product': product ,
    }

    # Renderizar la plantilla 'index.html' con el contexto
    return render(request, 'shop/product_detail.html', context)