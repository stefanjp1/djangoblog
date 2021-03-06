from django.contrib import admin

# Register your models here.
from myblog.models import Category
from myblog.models import Post

class CategoryAdmin(admin.ModelAdmin):
    pass

class CategoryInline(admin.StackedInline):
    model = Category.posts.through
    exclude = ('posts',)
    
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)