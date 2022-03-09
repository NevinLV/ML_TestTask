from django.conf import settings
from django.db import models

# Create your models here.
from CreateQuestion.models import Them


class Result(models.Model):
    them = models.ForeignKey(Them, on_delete=models.CASCADE, db_column='Them_id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='User_id')
    right = models.IntegerField('right')
    wrong = models.IntegerField('wrong')

    class Meta:
        db_table = 'Result'