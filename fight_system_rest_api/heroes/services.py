from django.db.models import Q
from random import randrange
from random import choice
from heroes.models import Hero 
from heroes.models import HeroRank
from heroes.models import Battle
from heroes.models import DeadHero
import heroes.serializer

class EmptyBattle(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class BattleService():
    
    @staticmethod
    def get_heroes_ranking(heroes_list):
        heroes_list = heroes_list.filter(dead =False)
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
        heroes_list = heroes_list.filter(dead=True)
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
        heroes_list = heroes_list.filter(dead=False)
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
                hero_oponents_list.append(heroes_oponents)
        hero_oponents_amount = len(hero_oponents_list)
        if hero_oponents_amount>0:
            random_index = randrange(0,hero_oponents_amount)
            hero1 = heroes_list[random_index]
            hero2 = choice(hero_oponents_list[random_index]) 
            result_battle = Battle()
            result_battle.fighter1 = hero1
            result_battle.fighter2 = hero2
            return result_battle
        else: 
            raise EmptyBattle('No possible battles to randomize')

