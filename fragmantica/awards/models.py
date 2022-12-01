#awards./models.py
from datetime import date

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

from fragmantica.core.model_mixins import StrFromFieldsMixin


class Award(StrFromFieldsMixin, models.Model):
	str_fields = ('name',)
	MIN_LEN_NAME=2
	MAX_LEN_NAME=64

	name=models.CharField(max_length=MAX_LEN_NAME, validators=(MinLengthValidator(MIN_LEN_NAME),),unique=True)
	image = models.URLField(null=False, blank=False, )
	slug = models.SlugField(unique=True, null=False, blank=True, )
	description = models.TextField()

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		if not self.slug:
			self.slug = slugify(f'{self.id}-{self.name}')

		return super().save(*args, **kwargs)