from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
# from .models import HeritageSite, HeritageSiteJurisdiction
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from .forms import HeritageSiteForm
# from django.urls import reverse_lazy
# from .filters import HeritageSiteFilter
# from django_filters.views import FilterView


class AboutPageView(generic.TemplateView):
	template_name = 'yelp/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'yelp/home.html'