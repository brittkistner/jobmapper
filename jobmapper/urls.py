from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from map.api.views import CompanyViewSet, KeywordViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, base_name='companies')
router.register(r'keywords', KeywordViewSet, base_name='keywords')


urlpatterns = patterns('',
   #REST
    # url(r'^', include(router.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #HOME PAGE
    url(r'^$', 'map.views.index', name='index'),

    # url(r'home/$', 'map.views.index', name='index'),


    url(r'^admin/', include(admin.site.urls)),
)
