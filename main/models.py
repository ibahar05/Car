from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    img = models.ImageField(default="https://www.bir23.com/images/default.jpg")

