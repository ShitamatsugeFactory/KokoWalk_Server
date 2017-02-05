from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ranking(models.Model):
    # marikoojisan / doitsujin / ....
    part = models.CharField(max_length=64)
    # user name
    name = models.CharField(max_length=64)
    score = models.IntegerField(null=True)
