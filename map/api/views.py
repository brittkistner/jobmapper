import json
import urllib
# import django_filters
from django.core import serializers
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from map.api.serializers import CompanySerializer, KeywordSerializer
from map.models import Company, Keyword


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # filter_fields = ('id',)

    #Return a set of companies based on location, industry, and keyword searches
    @list_route()
    def get_companies_by_location(self, request):
        #Get location data and pass through google api geocoder
        location = self.request.QUERY_PARAMS.get('location', None)
        request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(location)
        # request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(location, GOOGLE_API_KEY)
        data = json.loads(urllib.urlopen(request).read())

        #Get keywords and split strings into array
        keywords = self.request.QUERY_PARAMS.get('keywords', None)
        keywords = keywords.split(',')

        if data['status'] == 'OK':
            my_lat = data['results'][0]['geometry']['location']['lat']
            my_lng = data['results'][0]['geometry']['location']['lng']
            queryset = Company.objects.all()

            #Filter companies my the minimum and maximum latitude and longitude to form a square range
            #Filter on keywords
            filter_query = queryset.filter(latitude__gt=my_lat-.01, latitude__lt=my_lat+.01, longitude__gt=my_lng-.01, longitude__lt=my_lng+.01, keywords__word__in=keywords)
            print filter_query
            location = {
                "latitude": my_lat,
                "longitude": my_lng
            }
            companies_serializer = CompanySerializer(filter_query, many=True)
            # location_serializer = json.dumps(location)
            # print location_serializer
            return Response(companies_serializer.data)

    #Industry details
    # industry = self.request.QUERY_PARAMS.get('industry', None)
    #check on the lower and uppercase to match industry
    #filter_query = queryset.filter(latitude__gt=my_lat-.01, latitude__lt=my_lat+.01, longitude__gt=my_lng-.01, longitude__lt=my_lng+.01, industry=industry)

    @list_route()
    def get_industries(self, request):
        companies = Company.objects.all()
        industries = []
        for company in companies:
            # need to check the key values if this actually works
            if company.industry.upper() not in industries and company.industry != '':
                industries.append({'name': company.industry.upper()})
        print industries
        data = json.dumps(industries)
        return Response(data)



class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Keyword