from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/createpost/', views.createpost, name='createpost'),
    path('<int:post_id>/', views.detailpost, name='detailpost'),
    path('<int:post_id>/edit/', views.editpost, name='editpost'),
    path('<int:post_id>/edit/savepost/', views.savepost, name='savepost'),
]