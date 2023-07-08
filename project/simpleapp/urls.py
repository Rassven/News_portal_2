from django.urls import path
# Импортируем созданное нами представление
from .views import ArticleList, AboutArticle, BestArticle


urlpatterns = [
    path('', ArticleList.as_view()),
    path('<int:pk>', AboutArticle.as_view()),
    path('best', BestArticle.as_view()),

]
