from django.conf.urls import patterns, include, url

from django.contrib import admin
from sentiment.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'django_project.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
