from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Personne(models.Model):
    class Genre(models.TextChoices):
        homme = "homme"
        femme = "femme"
    nom = models.fields.CharField(max_length=30)
    genre = models.fields.CharField(choices=Genre.choices, max_length=10)
    email = models.fields.EmailField(max_length=50)
    age = models.fields.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])

    class Meta:
        db_table='homme_femme'