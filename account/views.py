from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import RegisterForm

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # Перенаправим на логин после успеха


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('home')  # перенаправление после успеха

    def get_object(self, queryset=None):
        # Автоматически получаем профиль текущего пользователя (создаём при необходимости)
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
