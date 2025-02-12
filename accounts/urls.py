# accounts/urls.py
from django.urls import path
from .views import user_login, AuthorsAndSellersView

app_name = 'users'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('authors_and_sellers/', AuthorsAndSellersView.as_view(), name='authors_and_sellers'),  # Ensure this line is present
    # Other URL patterns
]
