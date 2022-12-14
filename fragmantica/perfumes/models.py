#perfumes/models.py
from datetime import date
from enum import Enum

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.utils.text import slugify

from fragmantica.awards.models import Award
from fragmantica.core.model_mixins import StrFromFieldsMixin
from fragmantica.designers.models import Designer
from fragmantica.notes.models import Note



class ChoicesEnumMixin:
	@classmethod
	def choiceslist(cls):
		choices = [(x.name, x.value) for x in cls]
		return choices

	@classmethod
	def max_len(cls):
		return max(len(name) for name, _ in cls.choiceslist())


class PerfumeCategory(ChoicesEnumMixin, Enum):
	female= 'Female'
	male = 'Male'
	unisex = 'Unisex'


class Perfume(StrFromFieldsMixin, models.Model):
	str_fields = ('name','released', )
	PERFUME_NAME_MAX_LEN=96
	PERFUME_NAME_MIN_LEN=2
	PERFUME_YEAR_MIN=1960
	PERFUME_YEAR_MAX=date.today().year#TODO - add auto year

	name=models.CharField(max_length=PERFUME_NAME_MAX_LEN, validators=(MinLengthValidator(PERFUME_NAME_MIN_LEN),), unique=True)
	released=models.IntegerField(validators=(MinValueValidator(PERFUME_YEAR_MIN),MaxValueValidator(PERFUME_YEAR_MAX),),)
	image = models.URLField(null=False,blank=False,)
	designer=models.ForeignKey(Designer, on_delete=models.RESTRICT,)
	note=models.ManyToManyField(Note,)
	award=models.OneToOneField(Award,on_delete=models.RESTRICT,null=True, blank=True,)
	perfume_category = models.CharField(choices=PerfumeCategory.choiceslist(), max_length=PerfumeCategory.max_len())
	slug = models.SlugField(unique=True, null=False, blank=True, )

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		if not self.slug:
			self.slug = slugify(f'{self.id}-{self.name}')

		return super().save(*args, **kwargs)
