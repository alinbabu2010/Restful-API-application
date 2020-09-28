from django.conf.urls import url
from countries import views

urlpatterns = [
    url(r'^api/countrie$', views.countries_list),
    url(r'^api/countires/(?P<pk>[0-9]+)$',views.countries_detail)
]
