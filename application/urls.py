from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^sample-a/$', views.Sample1View.as_view(), name='sample-a'),
    url(r'^sample-b/$', views.Sample2View.as_view(), name='sample-b'),
]