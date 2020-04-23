from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('account/', include('allauth.urls')),
    path("menu", views.menu, name="menu"),
]
