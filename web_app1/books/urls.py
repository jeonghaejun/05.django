from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # /book/
    path('', views.BooksModelView.as_view(), name='index'),
    # /books/book
    path('book/', views.BookList.as_view(), name='book_list'),
    # /books/book/99/
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    # /books/author/
    path('author/', views.AuthorList.as_view(), name='author_list'),
    # /books/author/99/
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    # /books/publisher/
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),
    # /books/publisher/99/
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(),
         name='publisher_detail'),

]
