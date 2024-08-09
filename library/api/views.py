from book.models import Book
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import Ever_borrowed_book

from .serializers import BookDetailSerializer, BookSerializer, UserSerializer


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class BookListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BorrowBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        borrowed_entry, _ = Ever_borrowed_book.objects.get_or_create(
            user=request.user)
        borrowed_entry.has_book = True
        borrowed_entry.save()
        book = get_object_or_404(Book, id=book_id)
        if book.is_checked_out:
            return Response({"detail": "Book already checked out"},
                            status=status.HTTP_400_BAD_REQUEST)
        book.is_checked_out = True
        book.borrowed_by = request.user
        book.borrowed_date = timezone.now()
        book.save()
        return Response({"detail": "Book borrowed successfully"},
                        status=status.HTTP_200_OK)


class ReturnBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if book.borrowed_by != request.user:
            return Response({"detail": "You did not borrow this book"},
                            status=status.HTTP_400_BAD_REQUEST)
        book.is_checked_out = False
        book.borrowed_by = None
        book.borrowed_date = None
        book.save()
        remaining_books = Book.objects.filter(
            borrowed_by=request.user).exists()
        if not remaining_books:
            borrowed_entry = Ever_borrowed_book.objects.get(user=request.user)
            borrowed_entry.has_book = False
            borrowed_entry.save()
        return Response({"detail": "Book returned successfully"},
                        status=status.HTTP_200_OK)


class UserBooksView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        books = Book.objects.filter(borrowed_by=user)
        serializer = BookDetailSerializer(books, many=True)
        return Response(serializer.data)
