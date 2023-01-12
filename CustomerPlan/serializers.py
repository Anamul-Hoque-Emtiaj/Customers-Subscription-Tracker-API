from rest_framework import serializers,status
from .models import CustomerModel,PlanModel,PurchaseModel,PhoneNumberModel
from rest_framework.validators import ValidationError
from datetime import datetime,timedelta

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

class PurchaseSerializer(serializers.Serializer):
    planId = serializers.IntegerField()
    phoneNumber = serializers.CharField(max_length=30)

    def validate(self,data):
        isID = PlanModel.objects.get(pk=data.get('planId'))
        isPhone = PhoneNumberModel.objects.filter(phoneNumber = data.get('phoneNumber'))
        if not isID:
            raise ValidationError(detail="Wrong plan_id given",code=status.HTTP_403_FORBIDDEN)
        
        if not isPhone:
            raise ValidationError(detail="Wrong phone number given",code=status.HTTP_403_FORBIDDEN)

        return super().validate(data)

    def create(self,validated_data):

        cus = PhoneNumberModel.objects.filter(phoneNumber = validated_data.get('phoneNumber')).values('customer')
        cid = cus[0]['customer']
        customer = CustomerModel.objects.get(pk = cid)

        plan = PlanModel.objects.get(pk=validated_data.get('planId'))
        dur = PlanModel.objects.filter(id=validated_data.get('planId')).values('planDuration')
        duration = dur[0]['planDuration']
        purchaseTime = datetime.now()
        planExpireDate = datetime.now()

        if duration== "MONTHLY":
            planExpireDate = planExpireDate + timedelta(days = 30)
        else:
            planExpireDate = planExpireDate + timedelta(days = 365)

        print(purchaseTime,planExpireDate)

        prevPurchase = PurchaseModel.objects.filter(customer=cid)
        if prevPurchase:
            PurchaseModel.objects.filter(customer=cid).update(plan = plan, purchaseTime = purchaseTime, planExpireDate=planExpireDate)
            print(prevPurchase)
            return validated_data
        else:
            purchase = PurchaseModel(customer = customer, plan = plan,purchaseTime = purchaseTime, planExpireDate = planExpireDate)
            purchase.save()
            return validated_data
