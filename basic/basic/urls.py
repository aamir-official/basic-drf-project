from django.conf.urls import patterns, include, url
from rest_framework import routers
from basic.core.views import UserViewSet


from django.contrib import admin
admin.autodiscover()


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
