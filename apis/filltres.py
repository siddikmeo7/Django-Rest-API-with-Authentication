import django_filters
from .models import Bill

class BillFilter(django_filters.FilterSet):
    is_active = django_filters.BooleanFilter(field_name='is_active', lookup_expr='exact', initial=True)
    class Meta:
        model = Bill
        fields = ['table', 'castumername', 'is_active']
