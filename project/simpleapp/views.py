# from django.shortcuts import render

# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Article
from datetime import datetime


class ArticleList(ListView):
    model = Article
    ordering = 'pub_time'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['empty'] = None  # ='Not null'
        return context


class AboutArticle(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['empty'] = None  # ='Not null'
        return context

# лучшая статья
class BestArticle(ListView):
    model = Article
    # queryset = Article.objects.all().order_by('-rating').first()
    queryset = Article.objects.order_by('-rating').first()  # set to '-rating'
    template_name = 'best_article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['empty'] = None  # ='Not null'
        return context