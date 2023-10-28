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
    car_year = models.DateField()

# - __str__ method to print a car make object
    def __str__(self):
        return self.name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date,  car_model, car_year, sentiment, id):
        # Dealer dealership
        self.dealership = dealership
        # Dealer name
        self.name = name
        # Dealer purchase
        self.purchase = purchase
        # Dealer review
        self.review = review
        # Location purchase_date
        self.purchase_date = purchase_date
        # Location car_make
        # Dealer car_model
        self.car_model = car_model
        # Dealer car_year
        self.car_year = car_year
        # Dealer sentiment
        self.sentiment = sentiment
        # Dealer id
        self.id = id

        def __str__(self):
            return "Reviewer: " + self.name + " Review: " + self.review