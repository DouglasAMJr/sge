from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'serie_number', 'created_at', 'update_at',)
    search_fields = ('title',)


admin.site.register(models.Product, ProductAdmin)
