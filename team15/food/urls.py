from food.views import RestaurantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurant', RestaurantViewSet, basename='/')
urlpatterns = router.urls