# from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Salesperson, Customer, AutomobileVO, Sale
from common.json import ModelEncoder
from django.http import JsonResponse
import json

# Create your views here.


class AutomobileVOEncoder(ModelEncoder):
    model = AutomobileVO
    properties = ["vin", "sold", "id"]


class SalespersonEncoder(ModelEncoder):
    model = Salesperson
    properties = ["first_name", "last_name", "employee_id", "id"]


class CustomerEncoder(ModelEncoder):
    model = Customer
    properties = ["first_name", "last_name", "address", "phone_number", "id"]


class SaleEncoder(ModelEncoder):
    model = Sale
    properties = ["automobile", "salesperson", "customer", "price", "id"]
    encoders = {"automobile": AutomobileVOEncoder(),
                "salesperson": SalespersonEncoder(),
                "customer": CustomerEncoder()
                }


@require_http_methods(["GET", "POST"])
def api_salespersons(request):
    if request.method == "GET":
        salesperson = Salesperson.objects.all()
        return JsonResponse(
            {"salespersons": salesperson},
            encoder=SalespersonEncoder,
        )
    else:
        try:
            content = json.loads(request.body)
            salesperson = Salesperson.objects.create(**content)
            return JsonResponse(
                salesperson,
                encoder=SalespersonEncoder,
                safe=False,
            )
        except Salesperson.DoesNotExist:
            return JsonResponse(
                {"message": "Could not create salesperson"},
                status=400,
            )



@require_http_methods(["DELETE"])
def api_salesperson(request, pk):
    try:
        if request.method == "DELETE":
            salesperson = Salesperson.objects.get(id=pk)
            salesperson.delete()
            return JsonResponse(
                salesperson,
                encoder=SalespersonEncoder,
                safe=False,
            )
    except Salesperson.DoesNotExist:
        return JsonResponse({"message": "Does not exist"})


@require_http_methods(["GET", "POST"])
def api_customers(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        return JsonResponse(
            {"customers": customers},
            encoder=CustomerEncoder,
        )
    else:
        try:
            content = json.loads(request.body)
            customer = Customer.objects.create(**content)
            return JsonResponse(
                customer,
                encoder=CustomerEncoder,
                safe=False,
            )
        except Customer.DoesNotExist:
            return JsonResponse(
                {"message": "Could not create a customer"},
                status=400,
            )
