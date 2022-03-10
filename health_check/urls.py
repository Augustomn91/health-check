from django.urls import path
from health_check import views

app_name = 'server'

urlpatterns = [
    path('', views.ApplicationList.as_view(), name='application'),
]
