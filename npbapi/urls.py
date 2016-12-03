from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about', views.mail_form),
    url(r'^api', views.api),
    url(r'^score/today', views.today),
    url(r'^score/(?P<date_id>\d{8})/$', views.feedjson),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^scraper/update', views.update),
    url(r'^scraper/refresh', views.refresh),
]