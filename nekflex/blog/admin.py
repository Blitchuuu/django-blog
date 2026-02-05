from django.contrib import admin
from .models import Category, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at', 'is_featured')
    list_filter = ('status', 'is_featured', 'created_at', 'category')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('author__username', 'content')
