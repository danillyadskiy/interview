from rest_framework import viewsets

from companies.models import Company
from companies.serializers.company import CompanySerializer


class CompanySet(viewsets.ModelViewSet):
    queryset = Company.objects
    serializer_class = CompanySerializer
