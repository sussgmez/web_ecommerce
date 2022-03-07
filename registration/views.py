from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.contrib.auth import login
from .forms import NewUserForm

# Create your views here.
class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = NewUserForm
    success_url = '../home/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())
