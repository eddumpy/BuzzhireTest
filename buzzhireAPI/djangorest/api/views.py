from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer#, EventIdSerializer


class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventId(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('id')
