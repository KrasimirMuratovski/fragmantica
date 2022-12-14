from django.contrib import admin

from fragmantica.perfumes.models import Perfume


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name','perfume_category', 'released', 'designer', 'award')
	list_filter = ('name',  'perfume_category','released', 'designer', 'award')
	search_fields = ('name','perfume_category','released', 'designer', 'award')
