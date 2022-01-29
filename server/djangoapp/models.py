from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name, Description, and any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='Name')
    description = models.TextField(null=False, max_length=400, default='Description')
    state = models.CharField(null=False, max_length=100, default='State')
    
    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make 
class CarModel(models.Model):
    SEDAN = 'SEDAN'
    SUV = 'SUV'
    WAGON = 'WAGON'
    COUPE = 'COUPE' 
    PICKUP = 'PICKUP'
    OTHERS = 'OTHERS'
    TYPE = [
        (SEDAN, 'SEDAN'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON'),
        (COUPE, 'COUPE'),
        (PICKUP, 'PICKUP'),
        (OTHERS, 'OTHERS')
    ]

    carmake = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100, default='Name')
    dealer_id = models.IntegerField(null=True)
    type = models.CharField(null=True, max_length=20, choices=TYPE)
    year = models.DateField(null=True)

    def __str__(self):
        return self.name
    
# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
