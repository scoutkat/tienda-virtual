from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='categories'
   
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    precio = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'products')
    is_active=models.BooleanField(default=True)

    def __str__(self):
       return self.name
    
    @property
    def category_name(self):
       return self.category.name
   
    