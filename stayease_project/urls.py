"""
URL configuration for stayease_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('supply/', include('stayease_supply.urls')),
    path('sales/', include('stayease_sales.urls')),
    path('accounts/', include('stayease_accounts.urls')),
    path('operations/', include('stayease_operations.urls')),
    path('partners/', include('stayease_partners.urls')),
    path('contract/', include('property_details.urls')),
    path('tenant-details/', include('tenant_details.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    path('', include('stayease_app.urls')),
]
