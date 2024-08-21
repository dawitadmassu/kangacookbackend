from rest_framework import serializers
from .models import Customer, MealOrder

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone_number']




class MealOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = MealOrder
        fields = ['id', 'meal_name', 'quantity', 'customer']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer, created = Customer.objects.get_or_create(
            phone_number=customer_data['phone_number'],
            defaults={'name': customer_data.get('name', '')}
        )

        # Update the customer name if it was provided and the customer was not newly created
        if not created and customer_data.get('name'):
            customer.name = customer_data['name']
            customer.save()

        order = MealOrder.objects.create(customer=customer, **validated_data)
        return order
