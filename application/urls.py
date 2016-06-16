from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^sample-a/$', views.SampleAView.as_view(), name='sample-a'),
    url(r'^sample-b/$', views.SampleBView.as_view(), name='sample-b'),
]