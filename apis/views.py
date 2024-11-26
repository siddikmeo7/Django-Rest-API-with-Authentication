from rest_framework.generics import *
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .filltres import BillFilter
from .serializers import *
from django.core.management import call_command
from django.http import JsonResponse
from django.views import View
from rest_framework.permissions import IsAuthenticated


class RunMigrationsView(View):
    def get(self, request, *args, **kwargs):
        try:
            call_command('makemigrations')
            call_command('migrate')
            return JsonResponse({'status': 'success', 'message': 'Migrations applied successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    permission_classes = [IsAuthenticated]
    

class DishListAPIView(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['name_dish',"prf_time", "time_category"] 
    search_fields = ['name_dish',"time_category"]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = super().get_queryset()
        price_min = self.request.query_params.get('price_min', None)
        price_max = self.request.query_params.get('price_max', None)
        if price_min and price_max:
            queryset = queryset.filter(price__gte=price_min, price__lte=price_max)
        return queryset
    
class DishCreateAPIView(CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]

class DishRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]


class DishDestroyAPIView(DestroyAPIView):
    queryset = Dish.objects.all()
    permission_classes = [IsAuthenticated]

class TableListAPIView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['type',"max_person",] 
    search_fields = ['type',]
    permission_classes = [IsAuthenticated]

class TableCreateAPIView(CreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]

class TableRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]


class TableDestroyAPIView(DestroyAPIView):
    queryset = Table.objects.all()
    permission_classes = [IsAuthenticated]




class BillListAPIView(ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = BillFilter
    filterset_fields = ['table', "castumername"] 
    search_fields = ['castumername']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        bill_id = self.request.query_params.get('bill_id', None)
        if bill_id:
            queryset = queryset.filter(id=bill_id)
        queryset = queryset.prefetch_related('orders')  
        return queryset



class BillCreateAPIView(CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

class BillRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        bill_id = self.request.query_params.get('bill_id', None)
        if bill_id: 
            queryset = queryset.filter(id=bill_id)
        queryset = queryset.prefetch_related('orders')  
        return queryset
    permission_classes = [IsAuthenticated]


class BillDestroyAPIView(DestroyAPIView):
    queryset = Bill.objects.all()
    permission_classes = [IsAuthenticated]


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['dish',"bill",] 
    search_fields = ['id',]
    permission_classes = [IsAuthenticated]      

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def perform_create(self, serializer):
        bill = serializer.validated_data.get('bill')
        if not bill.is_active:
            raise ValidationError(f"Bill with ID {bill.id} is not active and cannot be used to create an order.")
        serializer.save()
    permission_classes = [IsAuthenticated]
        
class OrderRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderDestroyAPIView(DestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
