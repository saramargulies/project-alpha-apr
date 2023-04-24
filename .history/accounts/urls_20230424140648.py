from django.urls import path
from accounts.views import user_login, logout_view, signup_view

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
]
