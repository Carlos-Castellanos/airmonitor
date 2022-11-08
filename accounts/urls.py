from django.urls import path
from .views import SingUpView
# from django.conf import settings


urlpatterns = [
     path("signup/", SingUpView.as_view(), name="signup"),
    

]