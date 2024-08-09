from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


User = get_user_model()


class ReaderCreationForm(UserCreationForm):
    address = forms.CharField(max_length=255, required=True,
                              help_text='Обязательное поле.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.reader
        return user


class LibrarianCreationForm(UserCreationForm):
    tab_number = forms.CharField(max_length=6, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.librarian
        return user
