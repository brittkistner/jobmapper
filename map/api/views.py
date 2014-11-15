from rest_framework import viewsets
from map.api.serializers import CompanySerializer
from map.models import Company

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # lookup_field = 'username'