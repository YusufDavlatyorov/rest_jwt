from django.urls import path
from rest_framework_simplejwt.views import(
    TokenObtainPairView, TokenRefreshView
)
from .views import Register, Logout

urlpatterns=[
    path('register', Register.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('token/refresh',TokenRefreshView.as_view()),
    path('logout', Logout.as_view())
]