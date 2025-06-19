from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin



urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('encrypt/', views.encrypt_view, name='encrypt'),
    path('decrypt/', views.decrypt_view, name='decrypt'),

    #path('success/', views.login_view, name='success'),  # You can create a separate view for success
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)