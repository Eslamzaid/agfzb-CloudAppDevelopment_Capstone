from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
# - Name
    name = models.CharField(max_length=100)
# - Description
    description = models.CharField(max_length=220)
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    car = models.ForeignKey(CarMake, models.CASCADE, default=0)
# - Name
    name = models.CharField(max_length=100)
# - Dealer id, used to refer a dealer created in cloudant database
    dealer_id = models.IntegerField()
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    CAR_CHOICES = [
        ('Sedan', "Sedan"),
        ('SUV', "SUV"),
        ('WAGON', "WAGON"),
    ]
    car_type = models.CharField(max_length=100,choices=CAR_CHOICES)
# - Year (DateField)
    year = models.DateField()

# - __str__ method to print a car make object
    def __str__(self):
        return self.name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
