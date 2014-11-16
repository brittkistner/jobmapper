from rest_framework import serializers
from map.models import Company, Keyword


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('assigned_key',
            # 'id',
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

    # def get_keywords(self, obj):
    #     return obj.keywords

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ("word", "company")