from django.contrib import admin

from .models import *

@admin.register(Samolot)
class SamolotAdmin(admin.ModelAdmin):
    pass
@admin.register(Przyloty)
class PrzylotyAdmin(admin.ModelAdmin):
    pass
@admin.register(Odloty)
class OdlotyAdmin(admin.ModelAdmin):
    pass