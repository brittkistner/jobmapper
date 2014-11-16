from django.db.models import Avg
from rest_framework import serializers
from map.models import Company, Keyword


class CompanySerializer(serializers.ModelSerializer):
    popularity = serializers.SerializerMethodField('get_popularity')

    class Meta:
        model = Company
        fields = ('assigned_key',
            # 'id',
                  'popularity',
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

    def get_popularity(self, obj):
        average_overall_rating_for_all_companies = Company.objects.all().aggregate(Avg('overall_rating'))['overall_rating__avg'] #Keep this for overall rating across all industries
        single_company_overall_rating = obj.overall_rating
        company_popularity_comparison = obj.overall_rating/average_overall_rating_for_all_companies
        return company_popularity_comparison


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ("word", "company")