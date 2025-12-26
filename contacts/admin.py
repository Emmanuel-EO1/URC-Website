from django.contrib import admin
from .models import Inquiry
# Register your models here.

class InquiryAdmin(admin.ModelAdmin):
    # Display key contact info and the property it relates to
    list_display = ('id', 'name', 'email', 'phone', 'is_resolved', 'contact_date', 'property')
    list_display_links = ('id', 'name')
    # Filter by resolution status and type (property related or general)
    list_filter = ('is_resolved', 'property')
    search_fields = ('name', 'email', 'message')
    # Allow staff to mark an inquiry as resolved directly from the table overview
    list_editable = ('is_resolved',) 

admin.site.register(Inquiry, InquiryAdmin)