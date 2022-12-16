#awards.admin.py

from django.contrib import admin

from fragmantica.awards.models import Award


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)
	search_fields = ('name',)