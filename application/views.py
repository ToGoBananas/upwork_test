from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse
from .models import SampleA, SampleB
from .helpers import parse_excel


class IndexView(TemplateView):
    template_name = 'index.html'


class SampleAView(CreateView):

    def post(self, request, *args, **kwargs):
        result = parse_excel(files=request.FILES, category_cell_name='Class',
                             money_cell_name='Total Purchase Dollars')

        SampleA.objects.create(purchases=result)
        return HttpResponse(status=200)


class SampleBView(CreateView):

    def post(self, request, *args, **kwargs):
        result = parse_excel(files=request.FILES, category_cell_name='Dryden Category',
                             money_cell_name='Savings')

        SampleB.objects.create(savings=result)
        return HttpResponse(status=200)