from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from sentiment import views


admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', index, name='index'),
    url(r'^$', views.api_root),
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
