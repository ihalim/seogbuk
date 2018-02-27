from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.map, name ='map'),
	url(r'^test/$', views.map2, name = 'map2'),
	url(r'^test2/$', views.map3, name = 'map3' ),
	url(r'^test3/$', views.map4, name = 'map4' ),
	url(r'^test4/$', views.map5, name = 'map5' ),
	]