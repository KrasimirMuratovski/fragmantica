from django.contrib import admin

from fragmantica.designers.models import Designer


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
	pass