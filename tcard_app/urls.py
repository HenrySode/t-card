from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login', views.login, name = 'login'),
    path('guests', views.guests, name = 'guests'),
    path('upload/', views.upload_data, name='upload_data'),
    path('generate_qr/', views.generate_qr, name='generate_qr'),
    path('event_details/', views.event_details, name='events'),
    path('scan/', views.card_scan, name='scan'),
]