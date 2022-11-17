from django.contrib import admin
from .models import Category, Product
# Register your models here.


class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}  # поле по которому будем создавать категорию


admin.site.register(Category,
                    AdminCategory)  # зарегистрирует в админке по классу Category способность добавлять категории (бд распростроняется на админку)


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'stock', 'image', 'description', 'avaliable', 'created', 'updated',
                    'price']
    list_filter = ['avaliable', 'created', 'updated']
    list_editable = ['price', 'stock', 'avaliable']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, AdminProduct)
