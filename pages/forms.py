from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth import get_user_model
from .models import Recipe

CustomUser = get_user_model()


# - Create/Register a user(Model form)
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


# - Update profile

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'first_name', 'last_name', 'email', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'placeholder': 'Inserisci la tua bio', 'class': 'bio-textarea'}),
        }


# - Authenticate a user (Model form)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Creare una ricetta

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['image', 'title', 'description', 'ingredients', 'preparation', 'preparation_time', 'category']
        widgets = {
            'title': forms.Textarea(attrs={
                'placeholder': 'Inserisci il titolo',
                'class': 'textarea',
                'rows': 1,
                'cols': 40
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Inserisci la descrizione',
                'class': 'textarea',
                'rows': 2,
                'cols': 40
            }),
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'Inserisci gli ingredienti',
                'class': 'textarea',
                'rows': 2,
                'cols': 40
            }),
            'preparation': forms.Textarea(attrs={
                'placeholder': 'Inserisci la preparazione',
                'class': 'textarea',
                'rows': 2,
                'cols': 40
            }),
        }