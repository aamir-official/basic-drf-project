from django.conf.urls import include, url
from rest_framework import routers
from basic.core import views
import basic.browsable_api_with_non_model_viewset.urls

from django.contrib import admin
admin.autodiscover()


router = routers.DefaultRouter()
router.register(r'users', views.User)
router.register(r'my_user', views.MyUser)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^users2/$', views.UserList.as_view()),
    url(r'^example1/', include(basic.browsable_api_with_non_model_viewset.urls)),
    # url(r'^(?P<slug>\w+)/', include(router.urls)),
]
