#notes/admin.py
from django.contrib import admin
from fragmantica.notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'category')
	list_filter = ('name', 'category')
	search_fields = ('name','category')

