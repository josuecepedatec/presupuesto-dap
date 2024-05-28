from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Factura, Presupuesto, UserAreaOrSubArea
from .forms import LoginForm, FacturaForm
from .serializers import FacturaSerializer, PresupuestoSerializer, ExtraerMontoSerializer




def presupuestos_query(request):
    qs = Presupuesto.objects.all()
    if request.user.is_superuser:
        return qs
    try:
        u = UserAreaOrSubArea.objects.get(user=request.user)
        area = u.area
        sub_area = u.sub_area

        if area.nombre == 'General':
            return qs

        if sub_area and sub_area.nombre != 'No_Aplica':
            return qs.filter(area__id=area.pk, sub_area__id=sub_area.pk)
        if area:
            return qs.filter(area__id=area.pk)

    except UserAreaOrSubArea.DoesNotExist:
        pass
    return qs.none()

def user_context_data(request):
    user = request.user
    try:
        u = UserAreaOrSubArea.objects.get(user__id=user.pk)
        return {
            'is_superuser': request.user.is_superuser,
            'is_staff': request.user.is_staff,
            'puede_editar_monto': u.puede_editar_monto
        }
    except UserAreaOrSubArea.DoesNotExist:
        return {
            'is_superuser': request.user.is_superuser,
            'is_staff': request.user.is_staff,
            'puede_editar_monto': False
        }
    

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
def extraer_monto(request):
    if request.method == 'POST':
        serializer = ExtraerMontoSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data['presupuesto'] == serializer.data['presupuesto2']:
                return Response({'presupuesto': 'Selecciona diferentes presupuestos'}, status=status.HTTP_400_BAD_REQUEST)

            presupuesto = Presupuesto.objects.get(pk=serializer.data['presupuesto'])

            if serializer.data['cantidad'] > presupuesto.monto:
                return Response({'monto': f'la cantidad es mayor al monto restante de {presupuesto.presupuesto_id} - ${presupuesto.monto}'}, status=status.HTTP_400_BAD_REQUEST)

            presupuesto2 = Presupuesto.objects.get(pk=serializer.data['presupuesto2'])
            presupuesto2.monto += serializer.data['cantidad']
            presupuesto2.save()
            
            presupuesto.monto -= serializer.data['cantidad']
            presupuesto.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(" NO VALIDO")
        print(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    return render(request, 'index.html', context={
        'user_context_data': user_context_data(request)
    })


@login_required(redirect_field_name='next', login_url='/login/')
def editar_monto(request):
    context_data = user_context_data(request)
    if context_data['puede_editar_monto'] or context_data['is_superuser']:
        return render(request, 'editar-monto.html', context={
            'user_context_data': user_context_data(request)
        })
    return redirect(reverse('index'))

@login_required(redirect_field_name='next', login_url='/login/')
def facturas(request):
    presupuestos = presupuestos_query(request)
    facturas = Factura.objects.filter(presupuesto__in=presupuestos)

    paginator = Paginator(facturas, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'facturas.html', {'page_obj': page_obj, 'user_context_data': user_context_data(request)})


@login_required(redirect_field_name='next', login_url='/login/')
def presupuestos(request):
    presupuestos_list = presupuestos_query(request).annotate(num_facturas=Count('factura'))

    paginator = Paginator(presupuestos_list, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'presupuestos.html', {'page_obj': page_obj, 'user_context_data': user_context_data(request)})


class PresupuestoListView(APIView):
    def get(self, request):
        presupuestos = presupuestos_query(request)
        serializer = PresupuestoSerializer(presupuestos, many=True)
        return Response(serializer.data)