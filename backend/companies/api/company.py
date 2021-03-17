from rest_framework import viewsets

from companies.models import Company
from companies.serializers.company import CompanySerializer


class CompanySet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = Company.objects
        q = self.request.query_params.get('q')

        if q:
            queryset = queryset.filter(name__icontains=q) | \
                       queryset.filter(region__name__icontains=q)

        return queryset
