from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.CharField(max_length=100, default='URC Staff')
    body = models.TextField()
    cover_image = models.ImageField(upload_to='publications/%Y/%m/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('-publish_date',) 
        verbose_name_plural = "Articles & Publications"

    def __str__(self):
        return self.title