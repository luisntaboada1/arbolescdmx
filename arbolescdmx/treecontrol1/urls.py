from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'treecontrol1'
urlpatterns = [
    path('register-tree', views.tree_registration, name="tree_registration" )
]