from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login', views.login, name = 'login'),
    path('guests', views.guests, name = 'guests'),
    path('add_guest', views.add_guest, name = 'add_guest'),
    path('upload/', views.upload_data, name='upload'),
    path('event_details/', views.event_details, name='events'),
    path('register_event/', views.register_event, name='register_event'),
    path('generate_qr/', views.generate_qr, name='generate_qr'),
    path('scan/', views.card_scan, name='scan'),
]