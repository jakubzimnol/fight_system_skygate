from heroes.models import Hero, HeroRank, Battle, DeadHero
import heroes.serializer
from rest_framework import generics, status
from rest_framework.views import APIView
from django.db.models import Q
from random import randrange, choice
from django.contrib.auth.models import User
from rest_framework.response import Response


class HeroesList(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = heroes.serializer.HeroesSerializer
    
    
class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all() 
    serializer_class = heroes.serializer.HeroesSerializer
        
        
class HeroesRanking(generics.ListAPIView):

    def get_queryset(self ):
        heroes_list = Hero.objects.all().filter(dead =False)
        result = []
        num = heroes_list.count()
        for i in range( num ):
            herorank = HeroRank()
            hero_id = heroes_list[i]
            herorank.initialize( hero_id, hero_id.name, hero_id.get_wins_number(), hero_id.get_defeats_number() ) #battles_list.filter(winner_id = hero_id).count(), battles_list.filter( Q( Q(fighter1 = hero_id) | Q(fighter2 = hero_id)) & ~Q(winner_id=hero_id)).count() )
            result.append(herorank ) 
        result.sort(key=lambda herorank: herorank.wins, reverse=True)
        return result
    
    serializer_class = heroes.serializer.HeroesRankSerializer  
       
class HeroesDeads(generics.ListAPIView):

    def get_queryset(self ):
        heroes_list = Hero.objects.all().filter(dead =True)
        result = []
        num = heroes_list.count()
        for i in range( num ):
            hero_id = heroes_list[i]
            deadhero=DeadHero()
            deadhero.initialize( hero_id, hero_id.name, hero_id.date_of_death, hero_id.get_wins_number() )
            result.append(deadhero ) 
        result.sort(key=lambda deadhero: DeadHero.wins, reverse=True)
        return result
    
    serializer_class = heroes.serializer.DeadHeroesSerializer       
     
       
class HeroesKill(APIView):
    
    #queryset = Hero.objects.all() 
    #serializer_class = heroes.serializer.HeroesSerializer    
    
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
        hero_oponents_list = []
        num = heroes_list.count()
        for i in range( num ):
            heroes_oponents=[]
            for j in range( num ):
                if i!=j:
                    value = battles_list.filter( (Q(fighter1=heroes_list[i]) & Q(fighter2=heroes_list[j])) | (Q(fighter1=heroes_list[j]) & Q(fighter2=heroes_list[i])) ).count()
                    if (value==0) & (heroes_list[j].kind == heroes_list[i].kind):
                        heroes_oponents.append(heroes_list[j])
            if len(heroes_oponents)>0:
                print( len( heroes_oponents ) )
                hero_oponents_list.append(heroes_oponents)     
        n=len(hero_oponents_list)
        if n>0:
            random_index = randrange(0,n)
            hero1 = heroes_list[ random_index]
            hero2 = choice(hero_oponents_list[random_index] )
            
            result_battle = Battle()
            result_battle.fighter1 = hero1
            result_battle.fighter2 = hero2
            result_battle.save()
            serializer = heroes.serializer.BattleSerializer( data= result_battle.__dict__ )
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response( "no more battles possible", status=status.HTTP_400_BAD_REQUEST)
 
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = heroes.serializer.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = heroes.serializer.UserSerializer    