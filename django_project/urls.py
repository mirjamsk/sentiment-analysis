from django.conf.urls import patterns, include, url

from django.contrib import admin
from sentiment import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers


router = routers.DefaultRouter()


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

# API endpoints
urlpatterns += format_suffix_patterns([
    url(r'^posts/$',
        views.PostList.as_view(),
        name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$',
        views.PostDetail.as_view(),
        name='post-detail'),
    url(r'^comments/$',
        views.CommentList.as_view(),
        name='comment-list'),
    url(r'^comments/(?P<pk>[0-9]+)/$',
        views.CommentDetail.as_view(),
        name='comment-detail'),
])