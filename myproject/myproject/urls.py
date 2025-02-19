"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information, please refer to the Django documentation:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
Function views:
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')

Class-based views:
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')

Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

# Import necessary Django modules and views
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # URL pattern to serve media files in development (e.g., uploaded user files)
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    
    # URL pattern to serve static files in development (e.g., CSS, JS)
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    
    # Django admin interface
    path('admin/', admin.site.urls),

    # Homepage route, maps to the homepage view
    path('', views.homepage),

    # About page route, maps to the about page view
    path('about/', views.aboutpage),

    # Include URLs from the 'posts' app
    path('posts/', include('posts.urls')),

    # Include URLs from the 'users' app
    path('users/', include('users.urls')),
]

# Uncomment the next line for serving media files in development (for development only)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
