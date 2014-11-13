from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

#Example
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet, base_name='users')
# router.register(r'projects', ProjectViewSet, base_name='projects')


urlpatterns = patterns('',
   url(r'^', include(router.urls)),
   #DRF Routes
   # url(r'drf/$', 'map.views.', name=''),
   #Angular Endpoints
    url(r'^angular/$', 'map.views.index', name="index"),
    url(r'^admin/', include(admin.site.urls)),
)
