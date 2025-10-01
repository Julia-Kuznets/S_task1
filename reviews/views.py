from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.select_related('author', 'product').all()
