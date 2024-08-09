from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (BookListView, BorrowBookView, RegisterView, ReturnBookView,
                    UserBooksView)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:book_id>/borrow/', BorrowBookView.as_view(),
         name='borrow-book'),
    path('books/<int:book_id>/return/', ReturnBookView.as_view(),
         name='return-book'),
    path('my-books/', UserBooksView.as_view(), name='user-books'),
]
