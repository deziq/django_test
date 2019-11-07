from django.urls import path
from . import views

urlpatterns = [
    #Index url
    path('', views.index, name='index'),
    
    #book url 
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    
    # Author url
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:id>', views.AuthorDetailView.as_view(), name='author-detail'),

]