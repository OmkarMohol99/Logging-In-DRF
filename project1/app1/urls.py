from django.urls import path
from . import views


urlpatterns = [
    path('emp/', views.EmployeeApiView.as_view(), name='list-create'),
    path('emp/<int:pk>/', views.EmployeeDetails.as_view(), name='rud'),
    path('register/', views.SignupAPI.as_view(), name='register')
]