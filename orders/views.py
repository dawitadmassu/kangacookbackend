from rest_framework import viewsets
from .models import Customer, MealOrder
from .serializers import CustomerSerializer, MealOrderSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class MealOrderViewSet(viewsets.ModelViewSet):
    queryset = MealOrder.objects.all()
    serializer_class = MealOrderSerializer
