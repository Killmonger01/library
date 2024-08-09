from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=255, default='Untitled Book')
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    is_checked_out = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(User, null=True, blank=True,
                                    on_delete=models.SET_NULL)
    borrowed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
