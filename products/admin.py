from django.contrib import admin
from . import models



class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'date_inserted', 'description'
    ]


admin.site.register(models.ProductsModel, ProductsAdmin)
