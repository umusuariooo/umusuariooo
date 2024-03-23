from django.db import models
from datetime import datetime

class myfitness(models.Model):
    primeiro_nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    status = models.IntegerField()
    created_at = models.DateField(default=datetime.now)
    updated_at = models.DateField(default=datetime.now, blank=True)
