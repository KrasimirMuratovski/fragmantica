#common/admin.py

#
from django.contrib import admin

from fragmantica.common.models import PerfumeComment


@admin.register(PerfumeComment)
class PerfumeCommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'publication_date_and_time')
	list_filter = ('user','publication_date_and_time',)
	search_fields = ('user',)

