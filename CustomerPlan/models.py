from django.db import models

# Create your models here.
class PlanModel(models.Model):
    duration=(
        ('MONTHLY','Monthly'),
        ('YEARLY','Yearly')
    )
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    planDuration = models.CharField(max_length=7,choices=duration)

    def __str__(self):
        return f"Plan's name {self.name} , Price {self.planDuration} {self.price} BDT"

class CustomerModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"Name: {self.name}"

class PhoneNumberModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='phoneNumber')
    phoneNumber = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return f"{self.phoneNumber}"

class PurchaseModel(models.Model):
    customer = models.OneToOneField(CustomerModel, on_delete=models.CASCADE, related_name='plan')
    plan = models.ForeignKey(PlanModel, on_delete=models.SET_NULL,null=True)
    purchaseTime = models.DateTimeField(null=True)
    planExpireDate = models.DateTimeField(null=True)

    def __str__(self):
        return f"Customer {self.customer} purchase Plan {self.plan}. Expired at {self.planExpireDate}"