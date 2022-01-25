from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("edit", views.edit, name="edit"),
    path("do", views.do, name="do"),
    path("randompage", views.randompage, name="randompage"),
    path("<str:title>", views.title, name="title")
]
