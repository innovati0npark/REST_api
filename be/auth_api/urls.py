from django.urls import path
from auth_api.views import CustomAuthToken

urlpatterns = [
    path('api_token_auth/', CustomAuthToken.as_view()),
]