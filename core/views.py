from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Factura, Presupuesto
from .forms import LoginForm, FacturaForm
from .serializers import FacturaSerializer


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@api_view(['POST'])
def crear_factura(request):
    if request.method == 'POST':
        serializer = FacturaSerializer(data=request.data)
        if serializer.is_valid():
            presupuesto = Presupuesto.objects.get(pk=request.data['presupuesto'])
            subtotal = int(request.data['cantidad']) * float(request.data['precio_unitario'])

            if request.data.get('iva', None):
                total = subtotal * 1.16
            else:
                total = subtotal

            if total > presupuesto.monto:
                return Response({ 'monto':  'el total es mayor al monto restante'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                presupuesto.monto = presupuesto.monto - total
                presupuesto.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required(redirect_field_name='next', login_url='/login/')
def index(request):
    return render(request, 'index.html')

@login_required(redirect_field_name='next', login_url='/login/')
def facturas(request):
    return render(request, 'facturas.html')

@login_required(redirect_field_name='next', login_url='/login/')
def presupuestos(request):
    return render(request, 'presupuestos.html')

