from django.db import models

# Create your models here.

class TeamMember(models.Model):
    name= models.CharField(max_length=200)
    position= models.CharField(max_length=100)
    bio= models.TextField(blank=True)
    photo= models.ImageField(upload_to='team/%Y/%m', blank=True)
    is_featured= models.BooleanField(default=False)

    def __str__(self):
        return self.name