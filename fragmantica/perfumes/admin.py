from django.contrib import admin

from fragmantica.perfumes.models import Perfume


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'year', 'designer', 'award')
	list_filter = ('name',  'year', 'designer', 'award')
	search_fields = ('name', 'year', 'designer', 'award')
