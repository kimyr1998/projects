from django.urls import path
from . import views


app_name = 'programs'
urlpatterns = [
    # /books/
    path('', views.ProgramsModelView.as_view(), name='index'),

    # /books/book/
    path('program/', views.ProgramList.as_view(), name='program_list'),

    # /books/author/
    path('organ/', views.OrganList.as_view(), name='organ_list'),

    # /books/publisher/
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),

    # /books/book/99/
    path('program/<int:pk>/', views.ProgramDetail.as_view(), name='program_detail'),

    # /books/author/99/
    path('organ/<int:pk>/', views.OrganDetail.as_view(), name='organ_detail'),

    # /books/publisher/99/
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
]