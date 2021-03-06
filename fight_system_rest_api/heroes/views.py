from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
import heroes.serializer
from heroes.services import BattleService
from heroes.services import EmptyBattle
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
        heroes_list = Hero.objects.all()
        return BattleService.get_heroes_ranking(heroes_list)   
    
    serializer_class = heroes.serializer.HeroesRankSerializer  


class HeroesDeads(generics.ListAPIView):

    def get_queryset(self ):
        heroes_list = Hero.objects.all()
        return BattleService.get_dead_heroes(heroes_list)
    
    serializer_class = heroes.serializer.DeadHeroesSerializer       
     

class HeroesKill(viewsets.ViewSet):
    queryset = Hero.objects.all()
    serializer_class = heroes.serializer.HeroesReadOnlySerializer

    @action(methods=['patch'], detail=True)
    def kill(self, request, pk=None):
        hero = Hero.objects.all().filter(id=pk)[0]
        serializer = heroes.serializer.HeroesReadOnlySerializer(data=request.data)
        if serializer.is_valid():
            if hero.kill():
                hero.save()
                return Response({'status': 'hero is killed now'})
            else:
                return Response({'status': 'hero was killed before'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)            


class BattleList(generics.ListAPIView):
    queryset = Battle.objects.all() 
    serializer_class = heroes.serializer.BattleSerializer   
    
    
class BattleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Battle.objects.all() 
    serializer_class = heroes.serializer.BattleSerializer    
    

class BattleRandom(viewsets.ViewSet):
    queryset = Battle.objects.all()
    serializer_class = heroes.serializer.BattleReadOnlySerializer

    @action(methods=['post'], detail=False)
    def random(self, request):
        heroes_list = Hero.objects.all()
        battles_list = Battle.objects.all()
        try:
            randomized_battle = BattleService.random_heroes_for_fight(heroes_list, battles_list)
            serializer = heroes.serializer.BattleReadOnlySerializer(data=randomized_battle.__dict__)
            if serializer.is_valid():
                randomized_battle.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except EmptyBattle as e:
            return Response(e.value, status=status.HTTP_400_BAD_REQUEST)
        
        
 