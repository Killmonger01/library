from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомная модель пользователя."""
    reader = 'Читатель'
    librarian = 'Библиотекарь'
    ROLE_CHOICES = ((reader, 'Читатель'), (librarian, 'Библиотекарь'))
    username = models.CharField(
        verbose_name="никнейм",
        unique=True,
        max_length=50)
    first_name = models.CharField(verbose_name="Имя", max_length=30)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    role = models.CharField(verbose_name="Роль", choices=ROLE_CHOICES,
                            max_length=50)

    @property
    def is_reader(self):
        return self.role == User.reader

    @property
    def is_librarian(self):
        return self.role == User.librarian


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='reader_profile')
    address = models.CharField(verbose_name="адрес", max_length=255)


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='librarian_profile')
    tab_number = models.CharField(verbose_name="табельный номер",
                                  max_length=6,
                                  unique=True, blank=True, null=True)


class Ever_borrowed_book(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='ever_borrowed')
    has_book = models.BooleanField(default=False)
