from rest_framework import serializers
from map.models import Company


class CompanySerializer(serializers.ModelSerializer):
    #example
    # project_count = serializers.SerializerMethodField('get_project_count')

    class Meta:
        model = Company
        fields = ('id', 'name', 'street_address', 'city', 'state', 'zip_code', 'industry', 'latitude', 'longitude') #do i need this?

    #example
    # def get_project_count(self, obj):
    #     return obj.projects.count()