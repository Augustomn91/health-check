from django.urls import path
from health_check import views

app_name = 'server'

urlpatterns = [
    path('', views.ApplicationList.as_view(), name='application'),
    path('status/', views.StatusList.as_view(), name='status'),
]
