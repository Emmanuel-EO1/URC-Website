from django.contrib import admin
from .models import Property, PropertyImage, Agent
# Register your models here.

#--- Custom Admin Class for Property listings ---
class PropertyImageInline(admin.TabularInline):
    # Allows adding/editing multiple images directly within the Property creation form.
    model= PropertyImage
    extra= 3

class PropertyAdmin(admin.ModelAdmin):
    # What columns to show in the listings table overview
    list_display= ('id', 'title', 'price', 'is_featured', 'is_published', 'list_date', 'agent')
    # Make the title clickable to edit
    list_display_links= ('id', 'title')
    # Add a search bar to quickly find properties by title or address or city
    search_fields= ('title', 'address', 'city')
    # Add filters on the right sidebar to quickly narrow down listings
    list_filter= ('category', 'property_type', 'is_featured', 'is_published', 'city', 'agent')
    # Add an action dropdown 
    list_editable= ('is_published', 'is_featured')
    # Automatically generate the slug from the title as the agent types
    prepopulated_fields= {'slug': ('title',)}

    # Use the PropertyImageInline class to embed image fields
    inlines= [PropertyImageInline]

    # Organize the fields within the editing form
    fieldsets= (
        ('Property Status', {
            'fields': ('agent', 'category', 'property_type', 'is_published', 'is_featured'),
        }),
        ('Key Details', {
            'fields': ('title', 'slug', 'description', 'price'),
        }),
        ('Location & Specs', {
            'fields': ('address', 'city', 'bedrooms', 'bathrooms'),
        }),
        ('Visual Assets', {
            'fields': ('main_photo',),
        }),
    )

class AgentAdmin(admin.ModelAdmin):
    list_display= ('name', 'role', 'phone_number', 'email')
    list_display_links= ('name',)
    search_fields= ('name', 'email')


#--- Register Models to appear in Admin Panel ---
admin.site.register(Property, PropertyAdmin)
admin.site.register(Agent, AgentAdmin)

#PropertyImage is handed inline, so it's not registered separately.