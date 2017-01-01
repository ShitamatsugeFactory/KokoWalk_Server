# coding: utf-8

from django.conf.urls import url, include
from django.contrib import admin

from kokowalk.urls import router as kokowalk_router
from kokowalk.api import user_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # blog.urlsをincludeする
    url(r'^api/', include(kokowalk_router.urls)),
    url(r'^api/v1/counter/$', user_list),
    url(r'^api/counter/', include(kokowalk_router.urls)),
]