import pytz
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from user.models import Ever_borrowed_book, Reader

from .models import Book

User = get_user_model()


@login_required(login_url='user:login')
def index(request):
    now = timezone.now().astimezone(pytz.timezone('Europe/Moscow'))
    if request.user.role == User.reader:
        book_list = Book.objects.all()
        return render(request, 'book/index.html', {'book_list': book_list})
    elif request.user.role == User.librarian:
        books = []
        for book in Book.objects.filter(borrowed_by__isnull=False):
            days_borrowed = (now - book.borrowed_date.astimezone(
                pytz.timezone('Europe/Moscow'))).days
            address = Reader.objects.filter(user=book.borrowed_by)
            books.append({
                'username': book.borrowed_by.username,
                'first_name': book.borrowed_by.first_name,
                'last_name': book.borrowed_by.last_name,
                'title': book.title,
                'address': address[0].address,
                'borrowed_date': book.borrowed_date,
                'days_borrowed': days_borrowed,
            })
        return render(request, 'book/index.html', {'books': books})


@login_required
def borrow_book(request, book_id):
    borrowed_entry, _ = Ever_borrowed_book.objects.get_or_create(
        user=request.user)
    borrowed_entry.has_book = True
    borrowed_entry.save()

    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST' and book.borrowed_by is None:
        book.borrowed_by = request.user
        book.borrowed_date = timezone.now()
        book.is_checked_out = True
        book.save()

    return redirect('book:index')


@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST' and book.borrowed_by == request.user:
        book.borrowed_by = None
        book.is_checked_out = False
        book.save()
        remaining_books = Book.objects.filter(
            borrowed_by=request.user).exists()
        if not remaining_books:
            borrowed_entry = Ever_borrowed_book.objects.get(user=request.user)
            borrowed_entry.has_book = False
            borrowed_entry.save()
    return redirect('book:index')


def check_out_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not book.is_checked_out:
        book.is_checked_out = True
        book.checked_out_by = request.user
        book.save()
    return redirect('book:index')


@login_required
def my_books(request):
    now = timezone.now().astimezone(pytz.timezone('Europe/Moscow'))
    books = []
    for book in Book.objects.filter(borrowed_by=request.user):
        days_borrowed = (now - book.borrowed_date).days
        books.append({'title': book.title,
                      'borrowed_date': book.borrowed_date,
                      'days_borrowed': days_borrowed})
    return render(request, 'book/my_books.html', {'books': books})
