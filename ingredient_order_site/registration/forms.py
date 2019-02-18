from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff')
        labels = {"is_staff": "I'm a cook"}
        help_texts = {"is_staff": "Determines whether the user can create dishes."}
