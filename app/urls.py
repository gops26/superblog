from django.urls import path
from . import views
urlpatterns = [
    path("app/", views.home_view,name="home"),
    path("app/login/", views.login_view,name="login"),
    path("app/logout", views.logout_view,name="logout"),
    path("app/register", views.register_view,name="register_view"),
    path("app/write-blog", views.blog_upload,name="blogupload"),
    path("app/all-blogs", views.all_blogs,name="all-blogs"),
    path("app/my-blogs", views.my_blogs,name="my-blogs"),
    path("app/my-profile", views.profile_view, name="profile"),


]