from django.contrib import admin
from . models import WatchList,StreamPlatform,Review
# Register your models here.

class WatchListAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",)
    }
    list_display = ('title', "slug")

admin.site.register(WatchList,WatchListAdmin)

admin.site.register(StreamPlatform)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'description')

admin.site.register(Review)