from django.contrib import admin

# Register your models here.
from myblog.models import Category
from myblog.models import Post

admin.site.register(Post)
admin.site.register(Category)