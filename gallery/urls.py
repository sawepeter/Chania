from django.urls import path
from . import views
from django.contrib.auth.views import login

app_name = 'gallery'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', login, {'template_name': 'gallery/login.html'}, name='login'),

]