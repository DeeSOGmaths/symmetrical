from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin



urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('captcha/', views.captcha_view, name = 'captcha'),
    path('success/', views.captcha_view, name='success'),  # You can create a separate view for success
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)