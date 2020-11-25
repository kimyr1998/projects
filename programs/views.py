from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from programs.models import Program, Organ, Publisher


#--- TemplateView
class ProgramsModelView(TemplateView):
    template_name = 'programs/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Program', 'Organ', 'Publisher']
        return context


#--- ListView
class ProgramList(ListView):
    model = Program


class OrganList(ListView):
    model = Organ


class PublisherList(ListView):
    model = Publisher


#--- DetailView
class ProgramDetail(DetailView):
    model = Program


class OrganDetail(DetailView):
    model = Organ


class PublisherDetail(DetailView):
    model = Publisher

