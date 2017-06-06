from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.drawing_list, name='drawing_list'),
    url(r'^design/(?P<pk>\d+)/$', views.designer, name='designer'),
    url(r'^design/new/$', views.new_design, name='new_design'),
]