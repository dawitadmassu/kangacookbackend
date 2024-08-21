from django.core.validators import RegexValidator
from django.db import models

class Customer(models.Model):
    # Regex pattern for validating US phone numbers
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10}$',
        message="Phone number must be entered in the format: '+1234567890'. Up to 10 digits allowed."
    )
    
    name = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[phone_regex], max_length=15)  

    def __str__(self):
        return f"{self.name} ({self.phone_number})"


class MealOrder(models.Model):
    meal_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.customer.name} ordered {self.quantity} x {self.meal_name}"
