from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['author','title','text']}),
                 ('Date information', {'fields': ['created_date','published_date']})
                 ]
    list_display = ('title', 'text')
    search_fields = ['text']

admin.site.register(Post,PostAdmin)
# Register your models here.
