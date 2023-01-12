from django.contrib import admin
from .models import PlanModel, CustomerModel,PurchaseModel,PhoneNumberModel
# Register your models here.
admin.site.register(PlanModel)
admin.site.register(CustomerModel)
admin.site.register(PhoneNumberModel)
admin.site.register(PurchaseModel)