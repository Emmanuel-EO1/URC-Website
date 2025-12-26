from django.db import models
from django.utils import timezone
from listings.models import Property
# Create your models here.

class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, blank=True, null=True) 
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    contact_date = models.DateTimeField(default=timezone.now)
    is_resolved = models.BooleanField(default=False) 

    class Meta:
        verbose_name_plural = "Client Inquiries"

    def __str__(self):
        return f"Inquiry from {self.name} about {self.property.title if self.property else 'General'}"