from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:postid>', views.post, name="post"),
    re_path(r'^blog/postid/(\d+)', views.post, name="post")
]