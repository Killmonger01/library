from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow'),
    path('return/<int:book_id>/', views.return_book, name='return'),
    path('check_out/<int:book_id>/', views.check_out_book, name='check_out'),
    path('my-books/', views.my_books, name='my_books'),
]
