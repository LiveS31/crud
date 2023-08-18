from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, StockViewSet, test_page

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)
router.register('test', test_page)

urlpatterns = router.urls
