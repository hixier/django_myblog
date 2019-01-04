from django.contrib import admin
from .models import Author, Blog, Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_authors', 'blog_write_time')
    list_filter = ('title', 'blog_authors', 'blog_write_time')
    inlines = [CommentInline]


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('comment_authors', 'comment_write_time')
    list_display = ('display_commenttext', 'comment_authors', 'comment_write_time')


admin.site.register(Comment, CommentAdmin)


