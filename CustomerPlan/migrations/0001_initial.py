# Generated by Django 4.1.5 on 2023-01-11 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('planDuration', models.CharField(choices=[('MONTHLY', 'Monthly'), ('YEARLY', 'Yearly')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaseTime', models.DateTimeField()),
                ('planExpireDate', models.DateTimeField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CustomerPlan.customermodel')),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CustomerPlan.planmodel')),
            ],
        ),
    ]
