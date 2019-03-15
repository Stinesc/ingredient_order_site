from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import RegisterForm


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('registration:login')
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)
