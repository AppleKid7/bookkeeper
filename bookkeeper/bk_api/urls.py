from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bk_api import views


urlpatterns = [
    url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
    url(r'^users$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^groups$', views.GroupList.as_view()),
    url(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view()),
    url(r'^permissions$', views.PermissionList.as_view()),
    url(r'^permission/(?P<pk>[0-9]+)/$', views.PermissionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
