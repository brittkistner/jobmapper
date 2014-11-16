import json
import urllib
import django_filters
from rest_framework import generics
from rest_framework.response import Response
from map.api.serializers import CompanySerializer
from map.models import Company

class CompanyFilter(django_filters.FilterSet):

    min_latitude = django_filters.NumberFilter(name="latitude", lookup_type='gte')
    max_latitude = django_filters.NumberFilter(name="latitude", lookup_type='lte')
    min_longitude = django_filters.NumberFilter(name="longitude", lookup_type='gte')
    max_longitude = django_filters.NumberFilter(name="longitude", lookup_type='lte')

    class Meta:
        model = Company
        fields = ['min_latitude', 'max_latitude', 'min_longitude', 'max_longitude']

class CompanyList(generics.ListAPIView):
    # queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_class = CompanyFilter(generics.ListAPIView)
    # lookup_field = 'username'

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        #Get lat and long for searched placeName
        location = self.request.QUERY_PARAMS.get('location', None)
        request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(location)
        data = json.loads(urllib.urlopen(request).read())

        if data['status'] == 'OK':
            my_lat = data['results'][0]['geometry']['location']['lat']
            my_lng = data['results'][0]['geometry']['location']['lng']
            queryset = Company.objects.all()
            return queryset
            # test_query = queryset.filter(min_latitude=my_lat-.02, max_latitude=my_lat+.02, min_longitude=my_lng-.02, max_longitude=my_lng+.02)
            # companies = Company.objects.filter(latitude__range=(my_lat-.02, my_lat +.02), longi__range=(my_lng-.02, my_lng+.02), industry=industry, keywords)

#custom query example
# def get_queryset(self):
#         queryset = Project.objects.all()
#         active_status = self.request.QUERY_PARAMS.get('is_active', None)
#         if active_status is not None:  # Optionally filters against 'is_active' query param
#             queryset = queryset.filter(is_active=active_status)
#         return queryset

#search example
# # /users/?search=rudy searches across all listed fields
#     search_fields = ('first_name', 'last_name', 'about')


