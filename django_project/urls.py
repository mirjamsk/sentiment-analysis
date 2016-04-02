from django.conf.urls import patterns, include, url

from django.contrib import admin
from sentiment.views import *

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'django_project.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
