from heroes.models import Hero
import heroes.serializer #import 
from rest_framework import generics


class HeroesList(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = heroes.serializer.HeroesSerializer

class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all() 
    serializer_class = heroes.serializer.HeroesSerializer
        
class HeroesRanking(generics.ListAPIView):
    queryset = Hero.objects.all().order_by('name' )
    serializer_class = heroes.serializer.HeroesSerializer
    