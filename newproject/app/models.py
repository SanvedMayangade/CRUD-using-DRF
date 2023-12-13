from django.db import models

# Create your models here.
class Students(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    roll_no = models.IntegerField()
    adress = models.TextField()

    def __str__(self) -> str:
        return self.name