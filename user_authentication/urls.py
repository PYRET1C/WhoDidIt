from django.urls import path, include
from user_authentication import views

# TEMPLATE URLS
app_name = 'user_authentication'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login, name='user_login'),
]
