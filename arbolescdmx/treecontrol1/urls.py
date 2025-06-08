from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'treecontrol1'
urlpatterns = [
    path('register-tree', views.tree_registration, name="tree_registration" ),
    path('tree-index', views.tree_index, name='tree-index'),
    path('tree-delete/<int:pk>/', views.tree_delete, name='tree_delete'),
    path('tree-edit/<int:pk>/', views.tree_edit, name='tree_edit')
]