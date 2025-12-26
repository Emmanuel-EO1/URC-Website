from django.db import models

# Create your models here.

class Service(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()

    icon_class= models.CharField(max_length=50)
    is_active= models.BooleanField(default=True)

    class Meta:
        verbose_name_plural= 'Services Offered'

    def __str__(self):
        return self.title