from heroes.models import Hero
from heroes.serializer import HeroesSerializer
from rest_framework import generics


class HeroesList(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroesSerializer


class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroesSerializer