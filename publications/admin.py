from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display= ('title', 'publish_date', 'is_published')
    prepopulated_fields= {'slug': ('title',)}
    list_editable= ('is_published',)

admin.site.register(Article, ArticleAdmin)