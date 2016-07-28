"""Schedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from rest_framework import routers
from api import views

# router = routers.DefaultRouter()
# router.register(r'accounts',views.AccountViewSet)
#

accountlist = views.AccountViewSet.as_view(
{
    'get':'list',
    'post':'create'
}
)

urlpatterns = [
    #url(r'^',include(router.urls)),
    #url(r'^account/',include('account.urls')),
    url(r'^accounts/$',accountlist,name='account'),

]
