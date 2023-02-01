from django.urls import path
from .views import PlotsListView

urlpatterns = [
    path('apikey=<str:unique_key>', PlotsListView.as_view()),
]
