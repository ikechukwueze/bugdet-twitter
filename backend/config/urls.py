"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('tweets/', include('tweets.urls')),
    path('followers/', include('followers.urls')),
    path('timeline/', include('timeline.urls')),
    path('notifications/', include('notifications.urls')),
    path('trends/', include('trends.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('users.urls')),
#     path('api/', include('tweets.urls')),
#     path('api/', include('timeline.urls')),
#     path('api/', include('followers.urls')),
#     path('api/', include('notifications.urls')),
#     path('api/', include('search.urls')),
#     path('api/', include('messages.urls')),
# ]