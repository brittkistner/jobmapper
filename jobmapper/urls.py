from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from map.api.views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet, base_name='users')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    # url(r'rest/$', 'map.views.index', name='index'),
    url(r'angular/$', 'map.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
