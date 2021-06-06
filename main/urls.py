from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='home'),
    path('text_page', views.text_page, name='text'),
    path('tabl_page', views.tabl_page, name='tabl'),
    path('form_page', views.form_page, name='form'),
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),

]
