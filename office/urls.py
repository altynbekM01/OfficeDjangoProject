from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Register

app_name = 'office'
urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),


    path('api/show', views.showAllEmployers),
    path('api/position', views.showPositions),
    path('api/create', views.createEmployee),
    path('api/update/<str:pk>', views.updateEmployee),
    path('api/delete/<str:pk>', views.deleteEmployee),
    path('employees/', views.EmployeeAPIView.as_view()),
]