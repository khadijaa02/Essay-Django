from django.db import models

# Create your models here.
class CrudEssay(models.Model):
    field = models.CharField(max_length=20, help_text='Enter field documentation')