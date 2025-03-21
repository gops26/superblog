from django.urls import path
from . import views
urlpatterns = [
    path("app/", views.home_view,name="home"),
]