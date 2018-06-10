from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(regex=r'^create/$', view=views.create, name='create'),
    # url(regex=r'^info/(?P<business_name>\w+)/$', view=views.info, name='info'),
    # url(regex=r'^info/(?P<business_name>\w+)/employees/$', view=views.employees, name='employees'),
    url(regex=r'^info/(?P<business_name>\w+)/employees/add/$', view=views.addemployee, name='addemployee'),
    url(regex=r'^all/$', view=views.all_businesses, name='all_businesses'),

]