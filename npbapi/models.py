# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Scores(models.Model):
    inning = models.CharField(max_length=8)
    home_team = models.CharField(max_length=2)
    home_score = models.CharField(max_length=2)
    visitor_team = models.CharField(max_length=2)
    visitor_score = models.CharField(max_length=2)
    start_at = models.CharField(max_length=5)
    league = models.CharField(max_length=2)

class pastScore(models.Model):
    date = models.CharField(max_length=8)
    home_team = models.CharField(max_length=2)
    home_score = models.CharField(max_length=2)
    visitor_team = models.CharField(max_length=2)
    visitor_score = models.CharField(max_length=2)
    start_at = models.CharField(max_length=5)

class Mail(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    message = models.TextField()