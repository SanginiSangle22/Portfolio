from django.urls import path

from . import views


urlpatterns = [
    path("home/", views.home, name='home'),
    path("contact/", views.contact, name='contact'),
    path("service/", views.service, name='service'),
    path("portfolio/", views.portfolio, name='portfolio'),
    path("download/", views.download_resume, name='download'),
]

