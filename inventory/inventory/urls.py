"""
URL configuration for inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve
from attendance import views

urlpatterns = i18n_patterns(
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    path("admin/", admin.site.urls),
    path("filer/", include("filer.urls")),
    path("", include("cms.urls")),
    path("media/", serve, {"document_root": settings.MEDIA_ROOT}),
    path('admin_list', views.admin_list, name='admin-list'),
    path('admin_details/<int:pk>', views.admin_details, name='admin-details'),
    path('announcement_details/<int:pk>/', views.announcement_details,
         name='announcement-detail'),
    re_path(r"^attendance/api/admin_list/$", views.admin_list),
    re_path(r"^attendance/api/admin_details/([0-9])$", views.admin_details),
    re_path(r"^attendance/api/announcement_list/$", views.announcement_list),
    re_path(
        r"^attendance/api/announcement_details/([0-9])$", views.announcement_details),
    re_path(r"^attendance/api/employee_list/$", views.employee_list),
    re_path(
        r"^attendance/api/employee_details/([0-9])$", views.employee_details),
    re_path(r"^attendance/api/event_list/$", views.event_list),
    re_path(r"^attendance/api/event_details/([0-9])$", views.event_details),
    re_path(r"^attendance/api/mobile_scan_user_list/$",
            views.mobile_scan_user_list),
    re_path(r"^attendance/api/mobile_scan_user_details/([0-9])$",
            views.mobile_scan_user_details),
    re_path(r"^attendance/api/statictime_list/$", views.statictime_list),
    re_path(
        r"^attendance/api/statictime_details/([0-9])$", views.statictime_details),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('en/media/<path:path>', serve,
             {'document_root': settings.MEDIA_ROOT}),
    ]
