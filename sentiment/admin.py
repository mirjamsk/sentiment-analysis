from django.contrib import admin
from .models import ImPost, ImComment

# Register your models here.

class ImPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'likes', 'comments')

admin.site.register(ImPost, ImPostAdmin)
admin.site.register(ImComment)
