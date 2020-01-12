from django.shortcuts import render
from django.views.generic import FormView

from .forms import JoinForm
from .mixins import AjaxFormMixin

# Create your views here.
class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name = "forms/ajax.html"
    success_url = '/form-success/'

    

