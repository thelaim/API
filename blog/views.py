#from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ArticleSerializer
from .models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_date')
    serializer_class = ArticleSerializer
