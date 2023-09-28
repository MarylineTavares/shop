# Generated by Django 3.2.20 on 2023-09-13 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_shopper_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address_1', models.CharField(help_text='Adresse de voirie et numéro de rue', max_length=1500)),
                ('address_2', models.CharField(blank=True, help_text='Bâtiment, étage, lieu-dit', max_length=1500)),
                ('city', models.CharField(max_length=1500)),
                ('zip_code', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
