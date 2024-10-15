from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    #path('add/', views.addition, name='add'),
    #path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    #path('detail/', views.detail, name='detail'),
    #path('thank/', views.thank, name='thank')
]
