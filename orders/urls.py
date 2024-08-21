from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, MealOrderViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', MealOrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
