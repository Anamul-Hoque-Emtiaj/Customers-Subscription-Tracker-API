from django.shortcuts import render,get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import  CustomerModel, PlanModel,PhoneNumberModel
from .serializers import CustomerSerializer,PlanSerializer,PurchasePlanSerializer
from sequences import get_next_value
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class HomeView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary="home")
    def get(self, request):
        return Response(data={'Welcome to Home'}, status=status.HTTP_200_OK)

class RegisterView(generics.GenericAPIView):

    #generating unique BD phone number using django sequence
    def phoneNumberGenerator(self):
        num = get_next_value("phoneNumber1", initial_value=1500000000)
        phoneNumber = "+880"+str(num)
        return phoneNumber

    permission_classes=[IsAdminUser]
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer
    @swagger_auto_schema(operation_summary="Get Register page")
    def get(self, request):
        return Response(data={'Register new Customer'}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Register customer")
    def post(self, request):
        data = request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            id = serializer.data["id"]
            customer = CustomerModel.objects.get(pk=id)
            phoneNumber = self.phoneNumberGenerator()
            print(phoneNumber)
            customerPhoneNumber = PhoneNumberModel(customer=customer,phoneNumber=phoneNumber)
            customerPhoneNumber.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CustomerView(generics.GenericAPIView):
    permission_classes=[IsAdminUser]
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer
    
    @swagger_auto_schema(operation_summary="Get all customers info")
    def get(self, request):
        customer =  CustomerModel.objects.all()
        serializer=self.serializer_class(instance = customer, many = True)
        
        return Response(data=serializer.data , status=status.HTTP_200_OK)

class CustomerIDView(generics.GenericAPIView):
    permission_classes=[IsAdminUser]
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer

    @swagger_auto_schema(operation_summary="Get a customer info by its ID")
    def get(self, request,customer_id):
        customer = get_object_or_404(CustomerModel,pk=customer_id)
        serializer=self.serializer_class(instance = customer)
        return Response(data=serializer.data , status=status.HTTP_200_OK)

class PlanView(generics.GenericAPIView):

    queryset = PlanModel.objects.all()
    serializer_class = PlanSerializer
    @swagger_auto_schema(operation_summary="Get all plans info")
    def get(self, request):
        plan =  PlanModel.objects.all()
        serializer=self.serializer_class(instance = plan, many = True)
        return Response(data=serializer.data , status=status.HTTP_200_OK)

class PlanIDView(generics.GenericAPIView):
    queryset = PlanModel.objects.all()
    serializer_class = PlanSerializer

    @swagger_auto_schema(operation_summary="Get a plan info by its ID")
    def get(self, request, plan_id):
        plan = get_object_or_404(PlanModel,pk=plan_id)
        serializer=self.serializer_class(instance = plan)
        return Response(data=serializer.data , status=status.HTTP_200_OK)

class PurchasePlanView(generics.GenericAPIView):
    serializer_class = PurchasePlanSerializer
    permission_classes=[IsAdminUser]

    @swagger_auto_schema(operation_summary="Get purchase plan page")
    def get(self, request):
        return Response(data={"Purchase your Plan"} , status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="purchase a plan")
    def post(self, request):
        data = request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(operation_summary="purchase a new plan or renew your plan by paying subscription fee")
    def put(self, request):
        data = request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)