from django.contrib import admin
from .models import *


class CulturesAdmin(admin.ModelAdmin):
    model = Culture
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


class FarmersAdmin(admin.ModelAdmin):
    model = Farmer
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


class PlotsAdmin(admin.ModelAdmin):
    model = Plot
    list_display = ('id', 'farmer', 'culture', 'season')
    list_display_links = ('id',)
    search_fields = ('farmer__first_name', 'farmer__last_name', 'culture__name')
    list_filter = ('farmer', 'culture')


admin.site.register(Culture, CulturesAdmin)
admin.site.register(Farmer, FarmersAdmin)
admin.site.register(Plot, PlotsAdmin)
