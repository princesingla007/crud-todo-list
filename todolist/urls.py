from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("insert",views.insert,name="insert"),
    path("update/<id>",views.update,name="update"),
    path("delete/<id>",views.delete,name="delete"),

]