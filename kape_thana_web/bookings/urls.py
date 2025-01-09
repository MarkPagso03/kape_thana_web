from django.urls import path
from . import views


urlpatterns = [
    path('', views.booking, name="booking"),
    path('terms_and_condition', views.terms_and_condition, name="terms_and_condition")
    ]
