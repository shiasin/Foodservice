from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator, MinValueValidator,  MaxValueValidator
import datetime
# Create your models here.

class Workers(models.Model):
    positions={ 'MCH':'Master Chef',
                'CH':'Chef',
                'W':'Waiter',
                'CA':'Cashier'}

    name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    position = models.CharField(positions, max_length = 3)
    home_addr = models.CharField(max_length=1000)
    regex_phonenumber = RegexValidator(regex = r"0(21|26|25|86|24|23|81|28|31|44|11|74|83|51|45|17|41|54|87|71|66|34|56|13|77|76|61|38|58|35|84)[0-9]+")
    regex_mobilenumber = RegexValidator(regex = r"^(\+98|0)?9\d{9}",
                                        message = """your number isn't correct.
                                        true formats :
                                        1) +989999999999 2)09999999999""")
    # how many times using our service???
    phone_number = models.CharField(max_length=100, validators = [regex_phonenumber] )
    mobile_number = models.CharField(max_length=100, validators = [regex_mobilenumber])
    profile = models.ImageField(blank=False, null=False)
    published_date = models.DateField(default =  datetime.datetime.now())

#??????
class Table(models.Model):
    table_number = models.IntegerField(primary_key=True)
    table_availability = models.BooleanField(default = True)
    table_readyornot = models.BooleanField(default=True)
    reservation_state = models.BooleanField(default = False)

class OrderList(models.Model):
    #table or null
    table = models.ForeignKey(Table, related_name="OrderList_Table", on_delete= models.CASCADE)
    details = models.CharField(max_length=1000)
    #if takeaway= 1 then table ???
    takeaway = models.BooleanField(default=False)
    #?????
    cost = models.IntegerField(default = 0)

class FoodCategory(models.Model):
    category = models.CharField(max_length=100)

class Food(models.Model):
    food_name = models.CharField(unique=True, max_length = 100)
    food_details = models.CharField(max_length=1000)
    food_availability = models.BooleanField(default=True)
    cost = models.IntegerField(default = 0)
    food = models.ForeignKey(FoodCategory, related_name='Food_FoodCategory', on_delete=models.CASCADE)
    food_img = models.ImageField(blank = False, null = True)


class FoodOrder(models.Model):
    food = models.OneToOneField(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderList, related_name = 'FoodOrder_order',  on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
