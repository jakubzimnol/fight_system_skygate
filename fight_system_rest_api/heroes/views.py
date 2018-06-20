from heroes.models import Hero, HeroRank, Battle
import heroes.serializer #import 
from rest_framework import generics
from django.db.models import Q


class HeroesList(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = heroes.serializer.HeroesSerializer

class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all() 
    serializer_class = heroes.serializer.HeroesSerializer
        
class HeroesRanking(generics.ListAPIView):

    def get_queryset(self ):
        heroes_list = Hero.objects.all()
        #battles_list = Battle.objects.all()
        result = []
        num = heroes_list.count()
        for i in range( num ):
            herorank = HeroRank()
            hero_id = heroes_list[i]
            herorank.initialize( hero_id.name, hero_id.get_wins_number(), hero_id.get_defeats_number() ) #battles_list.filter(winner_id = hero_id).count(), battles_list.filter( Q( Q(fighter1 = hero_id) | Q(fighter2 = hero_id)) & ~Q(winner_id=hero_id)).count() )
            result.append(herorank )                     
        return result
    
    serializer_class = heroes.serializer.HeroesRankSerializer
        
    #def get_context_data(self, **kwargs):
        ## Call the base implementation first to get a context
        #context = super(HeroesRanking, self).get_context_data(**kwargs)
    
        ## Add in the publisher
        #context['wins'] = self.get_wins_number()
        #context['defeats'] = self.get_defeats_number()
        #return context ## Performing Extra Work    
       

class BattleList(generics.ListCreateAPIView):
    queryset = Battle.objects.all() 
    serializer_class = heroes.serializer.BattleSerializer    