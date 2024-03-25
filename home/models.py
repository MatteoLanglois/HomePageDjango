from django.db import models


class Project(models.Model):
    titre = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    nom = models.CharField(max_length=400)
    type = models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=300)
    visible = models.BooleanField(default=True)
