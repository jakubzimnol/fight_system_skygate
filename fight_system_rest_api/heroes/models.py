from django.db import models
from datetime import datetime  
from django.db.models import Q
from pygments.lexers import get_lexer_by_name


class HeroKind(models.Model):
    name = models.CharField(max_length=25, 
                            blank=True,
                            default=''
                            )
    def __str__(self):
        return self.name 


class HeroGroup(models.Model):
    name = models.CharField(max_length=25, 
                            blank=True,
                            default=''
                            )
    def __str__(self):
        return self.name 


class HeroBreed(models.Model):
    name = models.CharField(max_length=25, 
                            blank=True,
                            default=''
                            )       
    def __str__(self):
        return self.name


hero_kind1 = HeroKind(id=1, name = 'Big creature')
hero_kind1.save()
hero_kind2 = HeroKind(id=2, name = 'Medium creature')
hero_kind2.save() 
hero_kind3 = HeroKind(id=3, name = 'Small creature') 
hero_kind3.save()

hero_group1 = HeroGroup(id=1, name = 'Humanoid')
hero_group1.save()
hero_group2 = HeroGroup(id=2, name = 'Big plant')
hero_group2.save() 
hero_group3 = HeroGroup(id=3, name = 'Dragon') 
hero_group3.save()

hero_breed1 = HeroBreed(id=1, name = 'Human')
hero_breed1.save()
hero_breed2 = HeroBreed(id=2, name = 'Asgardian')
hero_breed2.save() 
hero_breed3 = HeroBreed(id=3, name = 'Frost Giant') 
hero_breed3.save() 


class Hero(models.Model):
   
    name = models.CharField(max_length=25, 
                            blank=True,
                            default=''
                            )
    created = models.DateTimeField(auto_now_add=True)
    kind = models.ForeignKey(HeroKind,
                             related_name='kind',  
                             null=True,
                             on_delete=models.SET_NULL,
                             )
    group = models.ForeignKey(HeroGroup,
                             related_name='group',  
                             null=True,
                             on_delete=models.SET_NULL,
                             )
    breed = models.ForeignKey(HeroBreed,
                             related_name='breed',  
                             null=True,
                             on_delete=models.SET_NULL,
                             )
    dead = models.BooleanField(default=False)
    date_of_death  = models.DateTimeField(auto_now_add=False,
                                          null=True
                                          )
    
    def kill(self):
        if self.dead == False:
            self.dead = True
            self.date_of_death = datetime.now()
            return True
        else:
            return False
        
    def get_wins_number(self):
        wining_battles = Battle.objects.filter(winner_id = self.id)
        return wining_battles.count()
        
    def get_defeats_number(self):
        losing_battles = Battle.objects.filter( Q( Q(fighter1 = self.id) | Q(fighter2 = self.id) ) 
                                                & ~Q(winner_id=self.id))
        return losing_battles.count()
        
    def __str__(self):
        return 'name = %s id = %s' % (self.name, self.id)  


class HeroRank(models.Model):
    hero = models.ForeignKey(Hero, 
                             related_name='hero',  
                             null=True,
                             on_delete=models.SET_NULL,
                            )
    name = models.CharField(max_length=25, 
                            blank=True, default='',
                            )
    wins = models.BigIntegerField(default=0)
    defeats = models.BigIntegerField(default=0)

    def initialize(self,
                   hero,
                   name,
                   wins,
                   defeats):
        self.hero = hero
        self.name = name
        self.wins = wins
        self.defeats = defeats
        
    def __str__(self):
        return 'hero name = %s wins = %s' % (self.hero.name, self.wins) 
    
    class Meta:
        managed = False


class DeadHero(models.Model):
    hero_id = models.ForeignKey(Hero, 
                                related_name='hero_id',
                                null=True,
                                on_delete=models.SET_NULL,
                                )
    name = models.CharField(max_length=25, 
                            blank=True,
                            default=''
                            )
    date_of_death  = models.DateTimeField(auto_now_add=False,
                                          null=True)
    wins = models.BigIntegerField(default=0)
    
    def initialize(self, 
                   dead_hero_id,
                   name,
                   date_of_death,
                   wins):
        self.hero_id = dead_hero_id
        self.name = name
        self.wins = wins
        self.date_of_death = date_of_death    
        
    def __str__(self):
        return 'hero name = %s wins = %s' % (self.hero.name, self.wins) 
    
    class Meta:
        managed = False    
    

class Battle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fighter1 = models.ForeignKey(Hero, 
                                 related_name='fighter1',
                                 on_delete=models.CASCADE,
                                 ) 
    fighter2 = models.ForeignKey(Hero, related_name='fighter2',
                                 on_delete=models.CASCADE
                                 )
    winner_id = models.ForeignKey(Hero,
                                  related_name='winner',
                                  on_delete=models.CASCADE, 
                                  null=True
                                  )
   
    def __str__(self):
        return 'id = %s fighter1 = %s' % (self.id, self.fighter1.name)    