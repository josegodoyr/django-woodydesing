from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name ='nosotros'),
    path('test', views.test, name ='test'),
    path('projects', views.projects, name ='projects'),
    path('projects/add_projects', views.add_projects, name ='add_projects'),
    path('projects/edit_projects/<int:id>', views.edit_projects, name ='edit_projects'),
    path('projects/delete_projects', views.delete_projects, name ='delete_projects'),
    ] 