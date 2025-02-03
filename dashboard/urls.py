from django.urls import path
from .views import home, add_bug, upload_data, analytics, bug_list

urlpatterns = [
    path('', home, name='home'),
    path('add-bug/', add_bug, name='add_bug'),
    path('upload-data/', upload_data, name='upload_data'),
    path('analytics/', analytics, name='analytics'),
    path('bugs/', bug_list, name='bug_list'),  # Added list view
]
