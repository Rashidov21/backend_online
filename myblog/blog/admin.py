from django.contrib import admin
from .models import Category,Comment,Contact,Post
# Register your models here.

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Post)
