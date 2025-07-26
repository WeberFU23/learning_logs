"""为users定义URL模式"""

from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView

app_name='users'
urlpatterns = [
    #注册页面
    path('register/',views.register,name='register'),
    #注销页面
    path('logout/', views.logout_view, name='logout'),
    #包含默认的身份验证URL，包含默认的注销页面，django默认调用前面的注销url模式
    path('',include('django.contrib.auth.urls')),
]