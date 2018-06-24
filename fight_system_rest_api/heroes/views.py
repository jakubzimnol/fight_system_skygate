import heroes.serializer
from rest_framework import generics
from rest_framework.views import APIView
from heroes.services import BattleService
from heroes.models import Hero
from heroes.models import Battle


class HeroesList(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = heroes.serializer.HeroesSerializer
    
    
class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all() 
    serializer_class = heroes.serializer.HeroesSerializer
        
        
class HeroesRanking(generics.ListAPIView):

    def get_queryset(self ):
        heroes_list = Hero.objects.all().filter(dead =False)
        return BattleService.get_heroes_ranking(heroes_list)   
    
    serializer_class = heroes.serializer.HeroesRankSerializer  


class HeroesDeads(generics.ListAPIView):

    def get_queryset(self ):
        heroes_list = Hero.objects.all().filter(dead =True)
        return BattleService.get_dead_heroes(heroes_list)
    
    serializer_class = heroes.serializer.DeadHeroesSerializer       
     
       
class HeroesKill(APIView):
      
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        hero = serializer.data.id
        hero.kill()
        hero.save()
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BattleList(generics.ListAPIView):
    queryset = Battle.objects.all() 
    serializer_class = heroes.serializer.BattleSerializer   
    
    
class BattleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Battle.objects.all() 
    serializer_class = heroes.serializer.BattleSerializer    
    

class BattleRandom(APIView):
    
    def post(self, request, *args, **kwargs):
        heroes_list = Hero.objects.all().filter(dead = False)
        battles_list = Battle.objects.all()
        return BattleService.random_heroes_for_fight(heroes_list, battles_list)
 