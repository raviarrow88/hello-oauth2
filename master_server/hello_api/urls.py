from django.conf.urls import url,include
from django.contrib import admin
from . import views
#from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/$', views.BookListView.as_view()),
    url(r'^books/(?P<id>\d+)/$', views.BookGetList.as_view()),
    url(r'^books/(?P<author>.+)/$', views.BookSearchList.as_view()),
    url(r'^api-token/permissions/$', views.PermissionView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)