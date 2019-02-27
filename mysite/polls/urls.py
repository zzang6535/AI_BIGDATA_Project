from django.urls import path, include

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.UserLoginView.as_view(), name='login'),  # 로그인
    path('logout/', LogoutView.as_view(), name='logout'),
]