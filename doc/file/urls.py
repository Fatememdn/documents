from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.UploadFileView.as_view()),
    path('edit/<int:pk>/', views.EditFileView.as_view()),
    path('delete/<int:pk>/', views.DeleteFileView.as_view()),
    path('list/', views.ListFileView.as_view()),
    path('ret/<int:pk>/', views.RetrieveFileView.as_view()),
]