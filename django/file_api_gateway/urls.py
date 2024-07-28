from django.urls import path
from file_api_gateway import views

urlpatterns = [
    path('files/', views.file_api_entry_point, name='file_api')
]
