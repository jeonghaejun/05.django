from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # /book/
    path('', views.BooksModelView.as_view(), name='index'),
    # /books/book
    path('book/', views.BookList.as_view(), name='book_list'),
]
