# Create your views here.
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy




class SingUpView(CreateView):
	form_class = UserCreationForm
	template_name = "registration/singup.html"
	sucess_url = reverse_lazy("login")

#SMPT


