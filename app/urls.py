from django.urls import path
from . import views
urlpatterns = [
    path("app/", views.home_view,name="home"),
    path("app/login/", views.login_view,name="login"),
    path("app/logout", views.logout_view,name="logout"),


]