from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from map.api.views import CompanyList

# router = routers.DefaultRouter()
# router.register(r'companies', CompanyList, base_name='users')

urlpatterns = patterns('',
    # url(r'^', include(router.urls)),
    url(r'companies', CompanyList.as_view(), name='companies'),
    # url(r'rest/$', 'map.views.index', name='index'),
    url(r'angular/$', 'map.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
