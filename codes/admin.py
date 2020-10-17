from django.contrib import admin
from .models import *

class LanguageAdmin(admin.ModelAdmin):
    search_fields = ['name', 'language_code', 'short_name', 'file_extension']
    list_display = ['name', 'language_code', 'short_name', 'file_extension', 'is_popular']
    ordering = ['-file_extension', '-short_name', 'name']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['body', 'author__username', 'code__snippet_title']
    list_display = ['author', 'body', 'code', 'datetime_utc']


class CodeAdmin(admin.ModelAdmin):
    
    def get_snippet_body(self, obj):
        snippet = obj.snippet_body
        return f"{snippet[:40]} ..." if len(snippet) > 40 else snippet
    
    search_fields = ['snippet_title', 'author__username', 'snippet_body', 'language__name', 'language__language_code']
    list_display = ["snippet_title", 'get_snippet_body', "language", "author", "total_views", "created_utc", "is_private"]


admin.site.register(Language, LanguageAdmin)
admin.site.register(Code, CodeAdmin)
admin.site.register(Comment, CommentAdmin)
