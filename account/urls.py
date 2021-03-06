from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('logout/',views.logout,name='logout'),
    path('register/', views.register, name='register'),
    path('authenticate/<str:uidb64>/<str:token>', views.authenticate, name='authenticate'),
    path('resend/<str:pk>', views.resend, name='resend'),
]