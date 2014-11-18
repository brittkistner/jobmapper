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

    #Return a set of companies based on location, industry, and keyword searches
    @list_route()
    def get_companies_by_location(self, request):

        #Get keywords and split strings into array
        keywords = self.request.QUERY_PARAMS.get('keywords', None)
        keywords = keywords.split(',')

        print keywords

        #Get industry value
        industry = self.request.QUERY_PARAMS.get('industry', None)
        print industry

        #Get location data and pass through google api geocoder
        location = self.request.QUERY_PARAMS.get('location', None)
        request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(location)
        # request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(location, GOOGLE_API_KEY)
        data = json.loads(urllib.urlopen(request).read())

        if data['status'] == 'OK':
            my_lat = data['results'][0]['geometry']['location']['lat']
            my_lng = data['results'][0]['geometry']['location']['lng']
            queryset = Company.objects.all()

            #Filter companies my the minimum and maximum latitude and longitude to form a square range
            # filter_query = queryset.filter(latitude__gt=my_lat-.01, latitude__lt=my_lat+.01, longitude__gt=my_lng-.01, longitude__lt=my_lng+.01, keywords__word__in=keywords)
            filter_query = queryset.filter(latitude__gt=my_lat-.01, latitude__lt=my_lat+.01, longitude__gt=my_lng-.01, longitude__lt=my_lng+.01, industry__iexact=industry, keywords__word__in=keywords)
            print filter_query
            location = {
                "latitude": my_lat,
                "longitude": my_lng
            }
            companies_serializer = CompanySerializer(filter_query, many=True)
            location_serializer = json.dumps(location)
            combined_object = {'location': location_serializer, 'companies': companies_serializer.data}
            data = json.dumps(combined_object)
            return Response(data)

    #Route to retrieve all non-duplicate industries within the Company table
    @list_route()
    def get_industries(self, request):
        companies = Company.objects.all()
        industries = []
        for company in companies:
            if not any(d['name'] == company.industry.upper() for d in industries) and company.industry != '':
                industries.append({'name': company.industry.upper()})
        data = json.dumps(industries)
        return Response(data)





class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Keyword