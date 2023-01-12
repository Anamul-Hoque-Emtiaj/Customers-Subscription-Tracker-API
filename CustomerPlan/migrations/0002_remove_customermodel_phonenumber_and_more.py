# Generated by Django 4.1.5 on 2023-01-11 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerPlan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customermodel',
            name='phoneNumber',
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='planExpireDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='PhoneNumberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=15, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerPlan.customermodel')),
            ],
        ),
    ]