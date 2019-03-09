from django.urls import path, include
from .views import index_view, logout_view, login_view, register_view
from django.contrib import auth


urlpatterns = [
    path('', index_view, name='home'),
    path('user_login/', login_view, name='user_login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

]