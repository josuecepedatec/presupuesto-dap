from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Factura, Presupuesto
from .forms import LoginForm, FacturaForm
from .serializers import FacturaSerializer, PresupuestoSerializer


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
            subtotal = float(request.data['cantidad']) * float(request.data['precio_unitario'])

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
    facturas = Factura.objects.all()
    paginator = Paginator(facturas, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'facturas.html', {'page_obj': page_obj})


@login_required(redirect_field_name='next', login_url='/login/')
def presupuestos(request):
    presupuestos_list = Presupuesto.objects.annotate(num_facturas=Count('factura'))
    paginator = Paginator(presupuestos_list, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'presupuestos.html', {'page_obj': page_obj})


class PresupuestoListView(APIView):
    def get(self, request):
        presupuestos = Presupuesto.objects.all()
        serializer = PresupuestoSerializer(presupuestos, many=True)
        return Response(serializer.data)