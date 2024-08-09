from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'genre', 'is_checked_out',
                    'borrowed_by', 'borrowed_date')
    list_filter = ('is_checked_out', 'author', 'genre', 'borrowed_by')
    search_fields = ('title', 'author', 'genre')
    readonly_fields = ('borrowed_date',)
