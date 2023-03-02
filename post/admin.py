from django.contrib import admin

from post.models import Author, Category, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)