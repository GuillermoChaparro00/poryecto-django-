
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app_coder.urls")),
    path("app_coder/", include("app_coder.urls"))
]
