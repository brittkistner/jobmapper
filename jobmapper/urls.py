from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
# from map.api.views import CompanyList
from map.api.views import CompanyViewSet, KeywordViewSet

router = routers.DefaultRouter()
# router.register(r'companies', CompanyList, base_name='companies')
router.register(r'companies', CompanyViewSet, base_name='companies')
router.register(r'keywords', KeywordViewSet, base_name='keywords')


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'companies', CompanyList.as_view(), name='companies'),
    url(r'angular/$', 'map.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
