from django.db import models
from django.utils import timezone
# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='agents/%Y/%m/', blank=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class Property(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, related_name='properties')
    PROPERTY_CATEGORY_CHOICES = [
    ('sale', 'For Sale'),
    ('rent', 'For Rent'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('flat', 'Flat / Apartment'),
        ('duplex', 'Duplex'),
        ('land', 'Land'),
        ('commercial', 'Commercial Property'),
    ]

    category= models.CharField(max_length=10, choices=PROPERTY_CATEGORY_CHOICES)
    property_type= models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)

    address= models.CharField(max_length=300)
    city= models.CharField(max_length=50, default='Lagos')
    description= models.TextField(blank=True)

    CURRENCY_CHOICES = [
        ('₦', 'NGN - Nigerian Naira'),
        ('$', 'USD - US Dollar'),
        ('€', 'EUR - Euro'),
        ('£', 'GBP - British Pound'),
        ('C$', 'CAD - Canadian Dollar'),
        ('¥', 'JPY - Japanese Yen'),
        ('GH₵', 'GHS - Ghanaian Cedi'),
    ]

    currency= models.CharField(max_length=5,choices=CURRENCY_CHOICES,default='₦')

    price= models.DecimalField(max_digits=14, decimal_places=2)
    bedrooms= models.IntegerField(default=0)
    bathrooms= models.IntegerField(default=0)

    main_photo= models.ImageField(upload_to='properties/%Y/%m/%d', blank=True)
    
    is_featured= models.BooleanField(default=False, verbose_name='Display on Homepage')
    is_published= models.BooleanField(default=True)
    list_date= models.DateTimeField(default=timezone.now)
    

    class Meta:
        verbose_name_plural = 'Property Listings'

    def __str__(self):
        return self.title
    
class PropertyImage(models.Model):
    property= models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image= models.ImageField(upload_to='properties/extra/%Y/%m/%d')

    def __str__(self):
        return f'Image for {self.property.title}'
