#awards.admin.py

from django.contrib import admin

from fragmantica.awards.models import Award


@admin.register(Award)
class DesignerAdmin(admin.ModelAdmin):
	pass