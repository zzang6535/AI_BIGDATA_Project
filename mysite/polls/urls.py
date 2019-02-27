from django.urls import path, include

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('load/', views.load, name='load'),

    path('create/', views.UserRegistrationView.as_view()),  # 회원가입
    path('login/', views.UserLoginView.as_view(), name='login'),  # 로그인
    path('logout/', LogoutView.as_view(), name='logout'),
]