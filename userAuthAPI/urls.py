from django.urls import path,include
from knox import views as knox_views

from .views import *

urlpatterns = [
    path('profile',UserProfileAPI.as_view()),
    path('register', RegisterAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('logout', knox_views.LogoutView.as_view(),name='knox_logout'),
]
