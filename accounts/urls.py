
from django.urls import path, include

from accounts.views import render_home, login_view, register_view, logout_view, profile_view, manage_databases, \
    DatabaseView
from rest_framework import routers

app_name="accounts"
router = routers.DefaultRouter()
router.register('databases',DatabaseView,'databases')

urlpatterns = [

    path('',render_home,name="home"),
    path('login/',login_view,name='login'),
    path('signup/',register_view, name="signup"),
    path('logout/',logout_view,name="logout"),
    path('profile/', profile_view, name="profile"),
    path('databases/', manage_databases, name="databases"),
    path('api/',include(router.urls))

]