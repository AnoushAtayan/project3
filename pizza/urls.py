from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("orders.urls")),
    path("accounts/", include("users.urls")),
    path("admin/", admin.site.urls),
]
