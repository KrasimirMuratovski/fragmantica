#designers/admin.py
from django.contrib import admin

from fragmantica.designers.models import Designer


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'since')
	list_filter = ('name', 'since')
	search_fields = ('name',)



# list_display = ('pk', 'publication_date', 'pets')
#
#
# @staticmethod
# def pets(current_photo_obj):
# 	tagged_pets = current_photo_obj.tagged_pets.all()
# 	if tagged_pets:
# 		return ', '.join(p.name for p in tagged_pets)
# 	return 'No pets'
