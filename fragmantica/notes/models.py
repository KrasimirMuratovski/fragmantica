#notes/models.py

from django.core.validators import MinLengthValidator
from django.db import models

from django.utils.text import slugify

from fragmantica.core.model_mixins import StrFromFieldsMixin


class Note(StrFromFieldsMixin, models.Model):
	str_fields = ('name',)
	NOTE_NAME_MAX_LEN=32
	NOTE_NAME_MIN_LEN=2


	name=models.CharField(max_length=NOTE_NAME_MAX_LEN, validators=(MinLengthValidator(NOTE_NAME_MIN_LEN),), unique=True)
	image = models.URLField(null=False,blank=False,)
	description=models.TextField()
	slug = models.SlugField(unique=True, null=False, blank=True, )

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		if not self.slug:
			self.slug = slugify(f'{self.id}-{self.name}')

		return super().save(*args, **kwargs)
