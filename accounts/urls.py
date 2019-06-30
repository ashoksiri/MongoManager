
from django.urls import path

from accounts.views import render_home, login_view, register_view

app_name="accounts"

urlpatterns = [

    path('home',render_home),
    path('login/',login_view,name='login'),
    path('signup/',register_view, name="signup")

]