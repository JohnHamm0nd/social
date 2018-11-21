from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(),name='home'),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('bye/',views.ByePage.as_view(),name='bye'),
    path('groups/',include('groups.urls')),
]
