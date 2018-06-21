from heroes.models import Hero, HeroRank, Battle
import heroes.serializer #import 
from rest_framework import generics
from django.db.models import Q
from random import randrange, choice


class HeroesList(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = heroes.serializer.HeroesSerializer
    
    
class HeroesCreate(generics.CreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = heroes.serializer.HeroesSerializerShort


class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all() 
    serializer_class = heroes.serializer.HeroesSerializer
        
#class HeoresKill(generics.UpdateView):
    ##model = Hero
    ##fields = ['name']
    ##template_name_suffix = '_update_form'
    #queryset = Hero.objects.all() 
    #serializer_class = heroes.serializer.HeroesSerializer    
    #self.kill()
        
class HeroesRanking(generics.ListAPIView):

    def get_queryset(self ):
        heroes_list = Hero.objects.all().filter(dead =False)
        #battles_list = Battle.objects.all()
        result = []
        num = heroes_list.count()
        for i in range( num ):
            herorank = HeroRank()
            hero_id = heroes_list[i]
            herorank.initialize( hero_id, hero_id.get_wins_number(), hero_id.get_defeats_number() ) #battles_list.filter(winner_id = hero_id).count(), battles_list.filter( Q( Q(fighter1 = hero_id) | Q(fighter2 = hero_id)) & ~Q(winner_id=hero_id)).count() )
            result.append(herorank ) 
        result.sort(key=lambda herorank: herorank.wins, reverse=True)
        return result#sorted(result, key=lambda herorank: herorank.wins )
    
    serializer_class = heroes.serializer.HeroesRankSerializer
        
    #def get_context_data(self, **kwargs):
        ## Call the base implementation first to get a context
        #context = super(HeroesRanking, self).get_context_data(**kwargs)
    
        ## Add in the publisher
        #context['wins'] = self.get_wins_number()
        #context['defeats'] = self.get_defeats_number()
        #return context ## Performing Extra Work    
       
class DeadsHeroes(generics.ListAPIView):

    def get_queryset(self ):
        heroes_list = Hero.objects.all().filter(dead =True)
        #battles_list = Battle.objects.all()
        result = []
        num = heroes_list.count()
        for i in range( num ):
            herorank = HeroRank()
            hero_id = heroes_list[i]
            herorank.initialize( hero_id, hero_id.get_wins_number(), hero_id.get_defeats_number() ) #battles_list.filter(winner_id = hero_id).count(), battles_list.filter( Q( Q(fighter1 = hero_id) | Q(fighter2 = hero_id)) & ~Q(winner_id=hero_id)).count() )
            result.append(herorank ) 
        result.sort(key=lambda herorank: herorank.wins, reverse=True)
        return result#sorted(result, key=lambda herorank: herorank.wins )
    
    serializer_class = heroes.serializer.HeroesRankSerializer       
       

class BattleList(generics.ListAPIView):
    queryset = Battle.objects.all() 
    serializer_class = heroes.serializer.BattleSerializer   
    
class BattleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Battle.objects.all() 
    serializer_class = heroes.serializer.BattleSerializer    
    
class BattleRandom(generics.CreateAPIView):

    serializer_class = heroes.serializer.BattleSerializer
    
    def get_queryset(self ):
        heroes_list = Hero.objects.all().filter(dead = False)
        battles_list = Battle.objects.all()
        hero_oponents_list = []
        num = heroes_list.count()
        
        for i in range( num ):
            for j in range( num ):
                
                if battles_list.filter( Q(Q(fighter1=heroes_list[i]) & Q(fighter2=heroes_list[j])) | Q(Q(fighter1=heroes_list[j]) & Q(fighter2=heroes_list[i])) ).count()==0 & heroes_list[j].group == heroes_list[i].group:
                    heroes_oponents.append(heroes_list[j])
                    
            if heroes_oponents.count()>=0:
                hero_oponents_list.append(heroes_oponents)     
                
        #for i in range( num ):
            #heroes_oponents =   heroes_list.filter(  Q(battles_list.filter( Q(Q(fighter1=heroes_list[i]) & Q(fighter2=F(id))) | Q(Q(fighter1=F(id)) & Q(fighter2=heroes_list[i])) )).count()=0  )
            #if heroes_oponents.count()>=0:
                #hero_oponents_list.append(heroes_oponents)
        
        random_index = randrange(0,len(hero_oponents_list))
        #choice1 = random.choice( hero_oponents_list )
        hero1 = heroes_list.get(random_index)
        hero2 = choice(heroes_oponents[random_index] )
        
        result_battle = Battle()
        result_battle.fighter1 = hero1
        result_battle.fighter2 = hero2
        
        return result_battle