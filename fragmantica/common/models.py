#common/models.py
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from fragmantica.perfumes.models import Perfume

UserModel = get_user_model()

class PerfumeComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(max_length=MAX_TEXT_LENGTH,null=False,blank=False,)
    publication_date_and_time = models.DateTimeField(auto_now_add=True,null=False, blank=True,)
    perfume = models.ForeignKey(Perfume,on_delete=models.RESTRICT,null=False,blank=True,)
    user = models.ForeignKey(UserModel,on_delete=models.RESTRICT,)