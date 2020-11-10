from django.contrib import admin

from .forms import BookForm, BookFormSet
from .models import Author, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", "publisher", "topic",)
    search_fields = ("author", "publisher", "topic")
    list_editable = ("author", "publisher", "topic",)

    def get_changelist_form(self, request, **kwargs):
        kwargs["form"] = BookForm
        return super().get_changelist_form(request, **kwargs)

    def get_changelist_formset(self, request, **kwargs):
        kwargs['formset'] = BookFormSet
        return super().get_changelist_formset(request, **kwargs)


admin.site.register(Book, BookAdmin)
