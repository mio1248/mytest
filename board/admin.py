from django.contrib import admin

from .models import BoardPost


@admin.register(BoardPost)
class BoardPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at',)
    ordering = ('-id',)
