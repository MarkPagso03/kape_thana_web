from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('about_us', views.about_us, name="about_us"),
    path('accomodation', views.accomodation, name="accomodation"),
    path('news', views.news, name="news"),
]
