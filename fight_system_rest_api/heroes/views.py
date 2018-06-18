from heroes.models import Hero,Humanoid,Big_plant
from heroes.serializer import HeroesSerializer
from rest_framework import generics


class HeroesList(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    #queryset += Big_plant.objects.all()
    serializer_class = HeroesSerializer


class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all() 
    #queryset += Big_plant.objects.all()
    serializer_class = HeroesSerializer