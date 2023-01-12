from django.urls import path
from . import views  

urlpatterns = [
    path('', views.HomeView.as_view(),name='Home'),
    path('register', views.RegisterView.as_view(),name='Register'),
    path('customer', views.CustomerView.as_view(),name='Customers'),
    path('customer/<int:customer_id>', views.CustomerIDView.as_view(),name='Customer'),
    path('plan', views.PlanView.as_view(),name='Plans'),
    path('plan/<int:plan_id>', views.PlanIDView.as_view(),name='Plan'),
    path('purchase', views.PurchasePlanView.as_view(),name='PurchasePlan'),
]
