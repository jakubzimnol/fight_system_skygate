from heroes.models import Hero,Humanoid,Big_plant
from heroes.serializer import HeroesSerializer, SpecialHeroesSerializer
from rest_framework import generics


class HeroesList(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroesSerializer


class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all() 
    serializer_class = HeroesSerializer
    
class HumanoidsList(generics.ListCreateAPIView):
    queryset = Humanoid.objects.all() 
    serializer_class = SpecialHeroesSerializer    
    
class Big_plantsList(generics.ListCreateAPIView):
    queryset = Big_plant.objects.all() 
    serializer_class = SpecialHeroesSerializer      