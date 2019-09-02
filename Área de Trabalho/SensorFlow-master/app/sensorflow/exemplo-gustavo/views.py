from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models

'''
Category
'''
class CategoryCreateView(CreateView):

    model = models.Category
    template_name = 'category/form.html'
    fields = ['name']
    success_url = reverse_lazy('movie-list')


'''
Movies
'''
class MovieListView(ListView):

    model = models.Movie
    template_name = 'movie/list.html'

    # def get_queryset(self):
    #     return models.Movie.objects.filter(year__gte=1995)

'''
Movie
'''
class MovieDetailView(DetailView):

    model = models.Movie
    template_name = 'movie/detail.html'

'''
Movie
'''
class MovieCreateView(CreateView):

    model = models.Movie
    template_name = 'movie/form.html'
    fields = '__all__'
    success_url = reverse_lazy('movie-list')

'''
Movie
'''
class MovieUpdateView(UpdateView):

    model = models.Movie
    template_name = 'movie/form.html'
    fields = '__all__'
    success_url = reverse_lazy('movie-list')

'''
Movie
'''
class MovieDeleteView(DeleteView):

    model = models.Movie
    template_name = 'movie/delete.html'
    success_url = reverse_lazy('movie-list')