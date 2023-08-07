from django.contrib import admin
from apps.blog.models import Blog, BlogCategory, BlogTags

admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(BlogTags)