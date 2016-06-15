from django.shortcuts import render
from django.views.generic import TemplateView, View, CreateView
from django.http import JsonResponse, HttpResponse


class IndexView(TemplateView):
    template_name = 'index.html'


class Sample1View(CreateView):

    def post(self, request, *args, **kwargs):
        return HttpResponse(status=200)


class Sample2View(CreateView):

    def post(self, request, *args, **kwargs):
        return HttpResponse(status=200)