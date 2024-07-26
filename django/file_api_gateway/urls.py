from django.urls import path
from .views import file_api_entry_point

urlpatterns = [
    path('files/', file_api_entry_point, name='file_api')
]
