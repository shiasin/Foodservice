# Generated by Django 2.1.7 on 2019-03-19 15:49

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100, unique=True)),
                ('food_details', models.CharField(max_length=1000)),
                ('food_availability', models.BooleanField(default=True)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoodOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('food', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant_admin.Food')),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=1000)),
                ('takeaway', models.BooleanField(default=False)),
                ('cost', models.IntegerField(default=0)),
                ('food_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FoodOrder', to='restaurant_admin.FoodOrder')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('sub_name', models.CharField(max_length=100)),
                ('sub_birthDate', models.DateField()),
                ('sub_address', models.CharField(max_length=1000)),
                ('sub_phone', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='0(21|26|25|86|24|23|81|28|31|44|11|74|83|51|45|17|41|54|87|71|66|34|56|13|77|76|61|38|58|35|84)[0-9]+')])),
                ('sub_mobile_phone', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message="your number isn't correct.\n                                        true formats :\n                                        1) +989999999999 2)09999999999", regex='^(\\+98|0)?9\\d{9}')])),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_number', models.IntegerField(primary_key=True, serialize=False)),
                ('table_availability', models.BooleanField(default=True)),
                ('table_ready', models.BooleanField(default=True)),
                ('reservation_state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('f_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=3, verbose_name={'CA': 'Cashier', 'CH': 'Chef', 'MCH': 'Master Chef', 'W': 'Waitress'})),
                ('home_addr', models.CharField(max_length=1000)),
                ('phone_number', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='0(21|26|25|86|24|23|81|28|31|44|11|74|83|51|45|17|41|54|87|71|66|34|56|13|77|76|61|38|58|35|84)[0-9]+')])),
                ('mobile_number', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message="your number isn't correct.\n                                        true formats :\n                                        1) +989999999999 2)09999999999", regex='^(\\+98|0)?9\\d{9}')])),
                ('published_date', models.DateField(default=datetime.datetime(2019, 3, 19, 15, 49, 42, 121065, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='orderlist',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrderList_Table', to='restaurant_admin.Table'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Food_FoodCategory', to='restaurant_admin.FoodCategory'),
        ),
    ]
