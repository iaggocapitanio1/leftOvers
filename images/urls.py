from rest_framework.routers import DefaultRouter

from . import views

app_name = 'images'
namespace = app_name
router = DefaultRouter()

router.register("image", views.ImageViewSet, basename="image")

urlpatterns = router.urls

