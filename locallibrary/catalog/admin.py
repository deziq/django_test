from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance

# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Define the admin class
class AuthorInstanceInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] | modifica l'odrine di visualizzazione
    inlines = [AuthorInstanceInline]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


#Genere dei libri
admin.site.register(Genre)


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book','status','due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('Anagrafica', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Disponibilità', {
            'fields': ('status', 'due_back')
        }),
    )