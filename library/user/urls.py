from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='user/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='user/login.html'),
         name='logout'),
]
