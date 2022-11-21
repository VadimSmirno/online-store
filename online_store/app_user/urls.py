from django.urls import path
from . import  views


urlpatterns = [
    path('register/', views.register, name= 'register_user'),
    path('personal_area/<int:pk>', views.UserDetaileViewPersonalArea.as_view(), name='personal_area'),
    path('logaut/', views.AuthenticationLogoutView.as_view(), name='logaut'),
    path('login/', views.AuthenticationLoginView.as_view(), name='login'),
    path('redact_profile/', views.RedactProfileView.as_view(), name='redact'),


]