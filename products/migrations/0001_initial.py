# Generated by Django 4.2.6 on 2023-11-01 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a product feature (e.g. Fan Kitchen-cabinet wardropes)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('title_document', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('specification', models.CharField(help_text='Enter a brief specification of the product', max_length=300)),
                ('location', models.CharField(help_text='Enter a the product location', max_length=300)),
                ('bedrooms', models.PositiveIntegerField(blank=True, null=True)),
                ('bathrooms', models.PositiveIntegerField(blank=True, null=True)),
                ('payment_duration', models.PositiveIntegerField(help_text='Enter a number in months e.g 18')),
                ('available_units', models.PositiveIntegerField(blank=True, null=True)),
                ('outright_payment', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Enter the outright payment price', max_digits=12, null=True)),
                ('mortgage_payment', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Enter the mortgage payment price', max_digits=12, null=True)),
                ('installmental_payment', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Enter installmental payment price', max_digits=12, null=True)),
                ('floor_area', models.PositiveBigIntegerField(help_text='Enter the net floor area for the product')),
                ('sales', models.CharField(blank=True, choices=[('Sold Out', 'Sold Out'), ('Now Selling', 'Now Selling'), ('On Request', 'On Request'), ('Not Available', 'Not Available')], default='Now Selling', help_text='Product sales status', max_length=50)),
                ('type', models.CharField(blank=True, choices=[('Land', 'Land'), ('Building', 'Building')], default='Building', help_text='Product type status', max_length=50)),
                ('features', models.ManyToManyField(help_text='Select a feature for this product', to='products.feature')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProdPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodphoto', to='products.product')),
            ],
        ),
    ]