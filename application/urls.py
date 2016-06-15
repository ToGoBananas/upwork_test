from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^sample1/$', views.Sample1View.as_view(), name='sample1'),
    url(r'^sample2/$', views.Sample2View.as_view(), name='sample2'),
]