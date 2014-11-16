import json
import urllib
# import django_filters
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from map.api.serializers import CompanySerializer
from map.models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    filter_fields = ('id',)

    @list_route()
    def get_companies_by_location(self, request):
        #Get lat and long for searched placeName
        location = self.request.QUERY_PARAMS.get('location', None)
        request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(location)
        # request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(location, GOOGLE_API_KEY)
        data = json.loads(urllib.urlopen(request).read())

        if data['status'] == 'OK':
            my_lat = data['results'][0]['geometry']['location']['lat']
            my_lng = data['results'][0]['geometry']['location']['lng']
            queryset = Company.objects.all()
            test_query = queryset.filter(latitude__gt=my_lat-.01, latitude__lt=my_lat+.01, longitude__gt=my_lng-.01, longitude__lt=my_lng+.01)
            print test_query
            serializer = CompanySerializer(test_query, many=True)
            return Response(serializer.data)


# class KeywordViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     company = CompanySerializer(read_only=True)
#
#     class Meta:
#         model = Keyword