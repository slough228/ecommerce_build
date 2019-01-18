from django.contrib import admin
from .models import Product, Gallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Product


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title']

    class Meta:
        model = Product


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Gallery, GalleryAdmin)
