from django.shortcuts import render
from django.views import generic

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    num_book_articolo_il = Book.objects.filter(title__icontains='il').count()
    num_genres = Genre.objects.filter(name__icontains='t').count()


    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_articoli_il':num_book_articolo_il,
        'num_genres':num_genres,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context=context)


# Book list
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

# Book Detail
class BookDetailView(generic.DetailView):
    model = Book

# Author
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

#Author Detail
class AuthorDetailView(generic.DetailView):
    model = Author
