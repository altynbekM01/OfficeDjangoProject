
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django_filters.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from office.forms import UserCreationForm
from office.models import Employee
from django.http import JsonResponse, HttpResponseRedirect

from office.serializers import EmployeeSerializer, PositionSerializer
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

@csrf_exempt
def showPositions(request):

    if request.method == 'GET':
        list = Employee.objects.all()
        serializer = PositionSerializer(list, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def showAllEmployers(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/noAcces.html')
    if request.method == 'GET':
        list = Employee.objects.all().order_by("-joined_at")
        serializer = EmployeeSerializer(list, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def createEmployee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return Response('Employee deleted')



def sayHi(request):
    return render(request, 'office/list.html')



class EmployeeAPIView(LoginRequiredMixin, generics.ListCreateAPIView):
    search_fields = ['name','surname', 'middleName', 'position','joined_at','salary', 'chief']
    filter_backends = (filters.SearchFilter,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    raise_exception = True


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

