from django.contrib import admin

from fragmantica.perfumes.models import Perfume


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
	pass