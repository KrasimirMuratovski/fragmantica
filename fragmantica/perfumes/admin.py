from django.contrib import admin

from fragmantica.perfumes.models import Perfume


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'year_created', 'designer', 'award')
	list_filter = ('name',  'year_created', 'designer', 'award')
	search_fields = ('name', 'year_created', 'designer', 'award')
