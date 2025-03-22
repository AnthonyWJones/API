from django.conf import settings
from django.contrib import admin
from django.urls import path
from core_apps.user_auth.views import TestLoginView
from drf_spectacular.views import (
SpectacularAPIView,
SpectacularRedocView,
SpectacularSwaggerView,

)


urlpatterns = [

    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/swagger-ui", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/v1/redoc", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

]

admin.site.site_header = "BackEndProgrammer.com Admin"
admin.site.site_title = "BackEndProgrammer.com Admin Portal"
admin.site.index_title = "Welcome to BackEndProgrammer.com Admin Portal"

