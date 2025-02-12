from django.db import models

class Kitoblar(models.Model):
    sarlavha = models.CharField(max_length=200)
    muallif = models.CharField(max_length=150)
    nashriyot = models.CharField(max_length=200)
    yili = models.IntegerField()
    isbn = models.IntegerField()


