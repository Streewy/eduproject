import django.contrib

# Register your models here.
from django.contrib import admin

from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

django.contrib.admin.site.register(Blog, BlogAdmin)