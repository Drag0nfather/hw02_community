from django.urls import path

from . import views

urlpatterns = [
    path("group/<slug>/", views.group_posts),
    path("", views.index, name="index"),
    path("test/", views.group_posts, name="group-posts")
] 