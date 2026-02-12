from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView, ProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    # template_name указывает, где искать файл с формой
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # Сразу добавим выход из системы
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
]
