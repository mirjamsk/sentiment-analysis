from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# urlpatterns += format_suffix_patterns([
#     url(r'^posts/$',
#         views.post_listing,
#         name='post-list'),
#     url(r'^posts/(?P<pk>[0-9]+)/$',
#         views.PostDetail.as_view(),
#         name='post-detail'),
#     url(r'^comments/$',
#         views.comment_listing,
#         name='comment-list'),
#     url(r'^comments/(?P<pk>[0-9]+)/$',
#         views.CommentDetailView.as_view(),
#         name='comment-detail'),
# ])