# Generated by Django 5.0.4 on 2024-06-13 20:34

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product_Category')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Item Name')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999)], verbose_name='Price per piece')),
                ('supplier', models.CharField(max_length=50, verbose_name='Supplier Name')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantity-In-Stock')),
                ('prodcateg', models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='prod_cat', to='ims.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email address')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=15, region=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('order-placed', 'order-placed'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], max_length=50, verbose_name='Order  Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_orders', to=settings.AUTH_USER_MODEL, verbose_name='Approved By')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL, verbose_name='Ordered By')),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='ims.product', verbose_name='Product-to-order')),
            ],
            options={
                'ordering': ['-updated', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ims.product')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('reorder_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stock',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='ims.OrderProduct', to='ims.product'),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(through='ims.ProductCategory', to='ims.category'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=250)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.stock')),
            ],
        ),
    ]
