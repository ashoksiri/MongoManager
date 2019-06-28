
from django.urls import path

from accounts.views import render_home

app_name="accounts"

urlpatterns = [

    path('home',render_home),

]