import django_filters
from .models import add_flight


class add_flightFilter(django_filters.FilterSet):
    source = django_filters.CharFilter(field_name='source', lookup_expr='icontains')
    check_in_date = django_filters.DateTimeFilter(field_name='IsoDateTimeField', lookup_expr='icontains')

    class Meta:
        models = add_flight
