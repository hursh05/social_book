from django.urls import path
from .views import DataFetchView

urlpatterns = [
    path('fetch-data/', DataFetchView.as_view(), name='fetch_data'),
]
