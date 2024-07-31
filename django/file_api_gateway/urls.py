from django.urls import path
from file_api_gateway import views

urlpatterns = [
    path('files/', views.file_api_entry_point, name='file_api'),
    path('listUsers/', views.list_users, name='list_users'),
    path('listObj/', views.list_obj, name='list_obj'),
    path('deleteRecord/',
         views.delete_record, name='delete_records'),
]
