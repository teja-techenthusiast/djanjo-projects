from django.urls import path
from . import views
#adding views to the urlpattern
urlpatterns = [
    path('', views.tasklist, name='tasks'),



]