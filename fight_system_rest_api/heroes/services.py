from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from random import randrange
from random import choice
from heroes.models import Hero 
from heroes.models import HeroRank
from heroes.models import Battle
from heroes.models import DeadHero
import heroes.serializer

class BattleService():
    
    @staticmethod
    def get_heroes_ranking(heroes_list):
        result = []
        heroes_amount = heroes_list.count()
        for i in range(heroes_amount):
            hero_rank = HeroRank()
            hero_id = heroes_list[i]
            hero_rank.initialize(hero_id,
                                hero_id.name, 
                                hero_id.get_wins_number(),
                                hero_id.get_defeats_number()) 
            result.append(hero_rank ) 
        result.sort(key=lambda hero_rank: hero_rank.wins, reverse=True)
        return result

    @staticmethod    
    def get_dead_heroes(heroes_list):
        result = []
        heroes_amount = heroes_list.count()
        for i in range( heroes_amount):
            hero_id = heroes_list[i]
            dead_hero=DeadHero()
            dead_hero.initialize(hero_id,
                                hero_id.name,
                                hero_id.date_of_death,
                                hero_id.get_wins_number())
            result.append(dead_hero) 
        result.sort(key=lambda deadhero: DeadHero.wins, reverse=True)
        return result

    @staticmethod
    def random_heroes_for_fight(heroes_list, battles_list):
        hero_oponents_list = []
        heroes_amount = heroes_list.count()
        for i in range( heroes_amount):
            heroes_oponents = []
            for j in range(heroes_amount):
                if i!=j:
                    value = battles_list.filter( (Q(fighter1=heroes_list[i]) & Q(fighter2=heroes_list[j])) 
                                                 | (Q(fighter1=heroes_list[j]) & Q(fighter2=heroes_list[i])) ).count()
                    if (value==0) & (heroes_list[j].kind == heroes_list[i].kind):
                        heroes_oponents.append(heroes_list[j])
            if len(heroes_oponents)>0:
                print(len(heroes_oponents))
                hero_oponents_list.append(heroes_oponents)     
        n=len(hero_oponents_list)
        if n>0:
            random_index = randrange(0,n)
            hero1 = heroes_list[random_index]
            hero2 = choice(hero_oponents_list[random_index] ) 
            result_battle = Battle()
            result_battle.fighter1 = hero1
            result_battle.fighter2 = hero2
            result_battle.save()
            serializer = heroes.serializer.BattleSerializer(data=result_battle.__dict__)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("no more battles possible", status=status.HTTP_400_BAD_REQUEST)


