from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion',)

admin.site.register(Post,PostAdmin)
