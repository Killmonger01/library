from .forms import ReaderCreationForm, LibrarianCreationForm
from django.shortcuts import render, redirect
from .models import Reader, Librarian
import uuid


def signup(request):
    if request.method == 'POST':
        if request.POST.get('role') == 'Читатель':
            form = ReaderCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                Reader.objects.create(user=user,
                                      address=request.POST.get('address'))
                return redirect('user:login')
        else:
            form = LibrarianCreationForm(request.POST)
            print(form.errors)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                unique_tab_number = False
                while not unique_tab_number:
                    tab_number = str(uuid.uuid4().int)[:6]
                    if not Librarian.objects.filter(
                            tab_number=tab_number).exists():

                        unique_tab_number = True
                Librarian.objects.create(
                    user=user,
                    tab_number=tab_number
                )
                return redirect('user:login')
    form = ReaderCreationForm()
    return render(request, 'user/signup.html', {'form': form})
