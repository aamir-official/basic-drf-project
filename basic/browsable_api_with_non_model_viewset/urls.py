from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', views.User, base_name='users')
urlpatterns = router.urls
