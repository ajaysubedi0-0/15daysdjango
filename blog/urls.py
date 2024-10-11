from django.urls import path
from .views.main_view import home,create_blog,single_blog,delete_blog
from .views.auth_view import register,login

urlpatterns =[
    path("",home, name="home"),
    path("register/",register, name="register"),
    path("login/",login, name="login"),
    path("create/",create_blog, name="create"),
    path("<int:blog_id>",single_blog, name="blog_detail"),
    path("<int:blog_id>/delete",delete_blog,name="delete_blog")
]