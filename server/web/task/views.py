# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    # def list(self, request):
    #     queryset = Cat.objects.all().order_by('-created_at')
    #     serializer = CatSerializer(queryset, many=True)
    #     return Response(serializer.data)

# Create your views here.
