from django.urls import path
from .views import *


urlpatterns = [
    path('scan/create/', ScanCreateView.as_view()),
    path('all/', ScanListView.as_view()),
    path('scan/delete/<int:pk>/', ScanDeleteView.as_view()),
    path('scan/detailed/<int:pk>/', ScanDetailedView.as_view()),
    path('scan/update/<int:pk>/', ScanUpdateView.as_view()),
]