from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",)  # Пароли добавятся автоматически


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': '+998 XX XXX-XX-XX'})
        }

    # Дополнительная валидация (пример)
    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        # Простая проверка: содержит только цифры, +, -, пробелы
        import re
        if not re.match(r'^[\d\s\+\-\(\)]+$', phone):
            raise forms.ValidationError('Введите корректный номер телефона')
        return phone
