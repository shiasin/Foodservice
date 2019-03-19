from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
import uuid


class Worker(models.Model):
    positions = {'MCH': 'Master Chef',
                 'CH': 'Chef',
                 'W': 'Waitress',
                 'CA': 'Cashier'}

    name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    position = models.CharField(positions, max_length=3)
    home_addr = models.CharField(max_length=1000)
    regex_phoneNumber = RegexValidator(regex=r"0(21|26|25|86|24|23|81|28|31|44|11|74|83|51|45|17|41|54|87|71|66|34"
                                             r"|56|13|77|76|61|38|58|35|84)[0-9]+")
    regex_mobileNumber = RegexValidator(regex=r"^(\+98|0)?9\d{9}",
                                        message="""your number isn't correct.
                                        true formats :
                                        1) +989999999999 2)09999999999""")
    # how many times using our service???
    phone_number = models.CharField(max_length=100, validators=[regex_phoneNumber])
    mobile_number = models.CharField(max_length=100, validators=[regex_mobileNumber])
    # profile = models.ImageField(blank=False, null=False)
    published_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name+" "+self.f_name


# ??????
class Table(models.Model):
    table_number = models.IntegerField(primary_key=True)
    table_availability = models.BooleanField(default=True)
    table_ready = models.BooleanField(default=True)
    reservation_state = models.BooleanField(default=False)

    def __str__(self):
        return self.table_number


class FoodCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Food(models.Model):
    food_name = models.CharField(unique=True, max_length=100)
    food_details = models.CharField(max_length=1000)
    food_availability = models.BooleanField(default=True)
    cost = models.IntegerField(default=0)
    food_category = models.ForeignKey(FoodCategory, related_name='Food_FoodCategory', on_delete=models.CASCADE)
    # food_img = models.ImageField(blank=False, null=True)

    def __str__(self):
        return self.food_name


class FoodOrder(models.Model):
    food = models.OneToOneField(Food, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)


class OrderList(models.Model):
    # table or null
    table = models.ForeignKey(Table, related_name="OrderList_Table", on_delete=models.CASCADE)
    details = models.CharField(max_length=1000)
    # if takeaway= 1 then table ???
    takeaway = models.BooleanField(default=False)
    food_order = models.ForeignKey(FoodOrder, related_name='FoodOrder', on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)


class Subscription(models.Model):
    # or national code ????
    sub_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sub_name = models.CharField(max_length=100)
    sub_birthDate = models.DateField()
    sub_address = models.CharField(max_length=1000)
    regex_phoneNumber = RegexValidator(regex=r"0(21|26|25|86|24|23|81|28|31|44|11|74|83|51|45|17|41|54|87|71|66|34"
                                             r"|56|13|77|76|61|38|58|35|84)[0-9]+")
    regex_mobileNumber = RegexValidator(regex=r"^(\+98|0)?9\d{9}",
                                        message="""your number isn't correct.
                                        true formats :
                                        1) +989999999999 2)09999999999""")
    # how many times using our service???
    sub_phone = models.CharField(max_length=100, validators=[regex_phoneNumber])
    sub_mobile_phone = models.CharField(max_length=100, validators=[regex_mobileNumber])
