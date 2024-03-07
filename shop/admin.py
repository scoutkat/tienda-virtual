from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'precio', 'description', 'category', 'is_active')
    list_filter = ('category','is_active')  # Agrega un filtro por categoría en la interfaz de administración
    search_fields = ('name', 'description')  # Agrega un campo de búsqueda para nombre y descripción