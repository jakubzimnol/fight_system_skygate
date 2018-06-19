from heroes.models import Hero,Humanoid,Big_plant
import heroes.serializer #import HeroesSerializer, HumanoidSerializer, Big_plantSerializer
from rest_framework import generics


class HeroesList(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = heroes.serializer.HeroesSerializer

class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all() 
    serializer_class = heroes.serializer.HeroesSerializer
         
class HeroesRanking(generics.ListAPIView):
    queryset = Hero.filter()
    serializer_class = heroes.serializer.