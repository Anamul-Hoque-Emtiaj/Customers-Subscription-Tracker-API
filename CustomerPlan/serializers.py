from rest_framework import serializers
from .models import CustomerModel,PlanModel,PurchaseModel,PhoneNumberModel

class PlanSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    price = serializers.DecimalField(max_digits=7,decimal_places=2)
    planDuration = serializers.CharField(source='get_planDuration_display')

    class Meta:
        model = PlanModel
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    class Meta:
        model = PurchaseModel 
        fields = ['plan','purchaseTime','planExpireDate']

class PhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumberModel 
        fields = ['phoneNumber']

class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    plan = PurchaseSerializer(read_only=True)
    phoneNumber = PhoneNumberSerializer(many=True, read_only=True)
    class Meta:
        model = CustomerModel 
        fields = '__all__'