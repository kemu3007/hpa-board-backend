"""hpa_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter

from .board import views as board_views
from .master import views as master_views

router = DefaultRouter()
router.register('team', master_views.TeamViewSet)
router.register('news', master_views.NewsViewSet)
router.register('event', board_views.EventViewSet)
router.register('application', board_views.ApplicationViewSet)

api_patterns = [
    path('is_logged_in/', master_views.isLoggedIn.as_view()),
    path('', include(router.urls)),
]


urlpatterns = [
    path('admin/native/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/v1/', include(api_patterns)),
]
