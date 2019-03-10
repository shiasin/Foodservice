from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator, MinValueValidator,  MaxValueValidator
import uuid


class Subscription(models.Model):
    #or national code ????
    sub_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sub_name = models.CharField(max_length=100)
    sub_birthdate = models.DateField()
    sub_address = models.CharField(max_length=1000)
    regex_phonenumber = RegexValidator(regex = r"0(21|26|25|86|24|23|81|28|31|44|11|74|83|51|45|17|41|54|87|71|66|34|56|13|77|76|61|38|58|35|84)[0-9]+")
    regex_mobilenumber = RegexValidator(regex = r"^(\+98|0)?9\d{9}",
                                        message = """your number isn't correct.
                                        true formats :
                                        1) +989999999999 2)09999999999""")
    # how many times using our service???
    sub_phone = models.CharField(max_length=100, validators = [regex_phonenumber] )
    sub_mobile_phone = models.CharField(max_length=100, validators = [regex_mobilenumber])

    #ghazahaye pishnahadi?
