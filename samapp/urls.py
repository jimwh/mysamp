"""samapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from samapp.myapp import views

from rest_framework.schemas import get_schema_view

from rest_framework_swagger.views import get_swagger_view

from django.views.generic.base import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

API_TITLE = 'University-Student API'
API_DESCRIPTION = 'A Web API for creating and viewing University-Student data model.'
schema_view = get_schema_view(title=API_TITLE)
swagger_view = get_swagger_view(title=API_TITLE)


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

router.register(r'universities', views.UniversityViewSet)
router.register(r'students', views.StudentViewSet)

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # Wire up our API using automatic URL routing with a comparable prefix to our cloudhub deployments
    url(r'^$', RedirectView.as_view(url='/v1/api', permanent=False)),
    url(r'^v1/api/', include(router.urls)),

    # Additionally, we include login URLs for the browsable API.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^(?P<version>(v1))/openapi/', include('drf_openapi.urls')),
    url(r'^swagger/$', swagger_view),
    url(r'^schema/$', schema_view),

]

# For the time being, serve static files from django, even when running under gunicorn or other wsgi server.
# In production, static files should be served by Apache HTTPD, Nginx, a CDN, etc.
# ("./manage.py runserver" always serves static files as it is meant for local development.)
urlpatterns += staticfiles_urlpatterns()

# Add the debug toolbar when developing.
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
