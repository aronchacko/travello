from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='photos')
    des=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    teamname=models.CharField(max_length=250)
    teamimage=models.ImageField(upload_to='pics')
    teamdes=models.TextField()


    def __str__(self):
        return self.teamname