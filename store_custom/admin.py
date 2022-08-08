from statistics import mode
from django.contrib import admin
from store.admin import ProductAdmin
from store.models import Product
from tags.admin import TagAdmin
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.


class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
