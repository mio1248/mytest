from django.urls import path

from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('write/', views.board_create, name='board_create'),
    path('<int:post_id>/', views.board_detail, name='board_detail'),
    path('<int:post_id>/edit/', views.board_update, name='board_update'),
    path('<int:post_id>/delete/', views.board_delete, name='board_delete'),
]
