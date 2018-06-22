from django.contrib import admin
from .models import  Client, Post, Comment

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass