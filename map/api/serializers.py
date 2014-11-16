from rest_framework import serializers
from map.models import Company


class CompanySerializer(serializers.ModelSerializer):
    #example
    # project_count = serializers.SerializerMethodField('get_project_count')

    class Meta:
        model = Company
        fields = ('id',
                  'LICID',
                  'GDCID',
                  'name',
                  'street_address',
                  'city',
                  'state',
                  'zip_code',
                  'address',
                  'latitude',
                  'longitude',
                  'twitter',
                  'logo_url',
                  'description',
                  'company_type',
                  'tckr',
                  'founded_year',
                  'website_url',
                  'employee_count_range',
                  'stock_exchange',
                  'num_followers',
                  'overall_rating',
                  'rating_description',
                  'culture_values_rating',
                  'senior_leadership_rating',
                  'compensation_benefits_rating',
                  'career_opportunities_rating',
                  'work_life_balance_rating',
                  'number_ratings',
                  'industry',
                  )

    #example
    # def get_project_count(self, obj):
    #     return obj.projects.count()