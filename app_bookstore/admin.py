from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    read_only_fields = ('id', 'user_created', 'date_created', 'date_updated',)
    list_display = ('id', 'last_name', 'first_name', 'age',)

    def save_model(self, request, obj, form, change):
        if obj.id == None:
            obj.user_created = request.user
            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)


class BookAdmin(admin.ModelAdmin):
    read_only_fields = ('id', 'user_created', 'date_created', 'date_updated',)
    list_display = ('id', 'title', 'author',)

    def save_model(self, request, obj, form, change):
        if obj.id == None:
            obj.user_created = request.user
            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)