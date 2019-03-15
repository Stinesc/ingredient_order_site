from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff')
        labels = {"is_staff": _("I'm a cook")}
        help_texts = {"is_staff": _("Determines whether the user can create dishes.")}
