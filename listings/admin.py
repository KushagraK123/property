from django.contrib import admin
from .models import Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isPublished', 'price', 'list_date', 'realtor')
    list_display_links = ('title', 'id')
    list_filter = ('realtor', 'price')
    list_editable = ('isPublished', )
    search_fields = ('title', 'description', 'city', 'state', 'zipcode')
    list_per_page = 6


admin.site.register(Listing, ListingAdmin)
