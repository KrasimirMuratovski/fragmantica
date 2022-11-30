from django.contrib import admin

# Register your models here.
from fragmantica.notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	pass