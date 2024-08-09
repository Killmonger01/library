from django.contrib import admin
from .models import User, Reader, Librarian, Ever_borrowed_book


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role')
    list_filter = ('role',)
    search_fields = ('username', 'first_name', 'last_name')


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')
    search_fields = ('user__username', 'address')


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('user', 'tab_number')
    search_fields = ('user__username', 'tab_number')


class ReturnedBookFilter(admin.SimpleListFilter):
    title = 'возвращенные книги'
    parameter_name = 'returned'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Возвращены'),
            ('no', 'Не возвращены'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(returned=True)
        if self.value() == 'no':
            return queryset.filter(returned=False)
        return queryset


@admin.register(Ever_borrowed_book)
class EverBorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'has_book')
    search_fields = ('user__username',)
    list_filter = ('has_book',)
