from django.db import models


# Create your models here.
from django.db import models

# Create your models here.
#table for Seasonal flavors
class Flavors(models.Model):
    Name=models.CharField(max_length=50)
    Season=models.CharField(max_length=50)
    Price=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        #insert name and season to string
        return f"{self.Name} {self.Season}"
    
#table for ingredients inventory
class Ingredients(models.Model):
    Name=models.CharField(max_length=30)
    Quantity=models.IntegerField()
    Expiry=models.DateField()

    def __str__(self):
        #insert name and quantity to string
        return f"{self.Name} - {self.Quantity}units"
    
#table for Customer feedback
class Customer_Feedback(models.Model):
    Flavor_suggestion = models.TextField(blank=True)
    Allergy_concerns = models.TextField(blank=True)

    def __str__(self):
        #add sugg and allergies
        return f"Feedback on flavor : {self.Flavor_suggestion} allergic to:{self.Allergy_concerns}"


