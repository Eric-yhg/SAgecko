"""SAgecko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from SAgecko import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^admin_list/', views.sa_list,name="sa_list"),
    url(r'^add_admin_list/', views.index2,name="add_sa"),
    url(r'^pm/', views.pm,name="pm"),
    url(r'^sys/', views.sys,name="sys"),
    url(r'^ceshi/', views.ajax,name="ceshi"),
    url(r'^permission/', views.permission,name="permission"),
    url(r'^test/', views.index3,name="test"),
    url(r'^accounts/login/$', views.acc_login,name="acc_login"),
    url(r'^accounts/logout/$', views.acc_logout, name="acc_logout"),
]
