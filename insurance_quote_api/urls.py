from django.urls import path
from insurance_quote_api import views

urlpatterns = [
    path('quote/', views.QuoteApiView.as_view(), name='quote'),
]

