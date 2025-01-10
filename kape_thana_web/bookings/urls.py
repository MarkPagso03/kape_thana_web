from django.urls import path
from .views import InQueueListView, AcceptedListView, OnGoingListView, HistoryListView
from . import views


urlpatterns = [
    path('', views.booking, name="booking"),
    path('terms_and_condition', views.terms_and_condition, name="terms_and_condition"),
    path('api/InQueueListView/', InQueueListView.as_view(), name='InQueueList'),
    path('api/AcceptedListView/', AcceptedListView.as_view(), name='AcceptedList'),
    path('api/OnGoingListView/', OnGoingListView.as_view(), name='OnGoingList'),
    path('api/HistoryListView/', HistoryListView.as_view(), name='HistoryList'),
    path('update-or-delete-booking/', views.update_or_delete_booking, name='update_or_delete_booking'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/history', views.history, name='history')
    ]
