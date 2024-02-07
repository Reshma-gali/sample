import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

from employee.models import Employee
from APIS.v1.serializers import EmployeeSerializer


@csrf_exempt
def get_details(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        #print(request.body)
        data = JSONParser().parse(request)
        print(data)
        #data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        #print(data)
        emp_id=data.get('id')
        emp=Employee.objects.get(id=emp_id)
        serializer = EmployeeSerializer(emp,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        #print(data)
        emp_id=data.get('id')
        emp=Employee.objects.get(id=emp_id)
        serializer = EmployeeSerializer(emp,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        #print(data)
        emp_id=data.get('id')
        emp=Employee.objects.get(id=emp_id)
        emp.delete()
        return HttpResponse("Deleted")
    else:
        return HttpResponse("Invalid Request")