from django.shortcuts import render,get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import  CustomerModel, PlanModel,PurchaseModel
from .serializers import CustomerSerializer,PlanSerializer,PurchaseSerializer

# Create your views here.
class HomeView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={'Hello Home'}, status=status.HTTP_200_OK)

class CustomerView(generics.GenericAPIView):

    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request):
        customer =  CustomerModel.objects.all()
        serializer=self.serializer_class(instance = customer, many = True)
        print(serializer.data)
        return Response(data=serializer.data , status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer=self.serializer_class(data=data)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class CustomerIDView(generics.GenericAPIView):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer
    def get(self, request,customer_id):
        customer = get_object_or_404(CustomerModel,pk=customer_id)
        serializer=self.serializer_class(instance = customer)
        print(serializer.data)
        return Response(data=serializer.data , status=status.HTTP_200_OK)

class PlanView(generics.GenericAPIView):

    queryset = PlanModel.objects.all()
    serializer_class = PlanSerializer

    def get(self, request):
        plan =  PlanModel.objects.all()
        serializer=self.serializer_class(instance = plan, many = True)
        print(serializer.data)
        return Response(data=serializer.data , status=status.HTTP_200_OK)

class PlanIDView(generics.GenericAPIView):
    queryset = PlanModel.objects.all()
    serializer_class = PlanSerializer
    def get(self, request, plan_id):
        plan = get_object_or_404(PlanModel,pk=plan_id)
        serializer=self.serializer_class(instance = plan)
        print(serializer.data)
        return Response(data=serializer.data , status=status.HTTP_200_OK)
