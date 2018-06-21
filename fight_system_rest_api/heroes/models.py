from django.db import models
from datetime import datetime  
from django.db.models import Q

   
class Hero(models.Model):
    HEROES_KINDS = (
        ('B','Big creature'),
        ('M','Medium creature'),
        ('S','Small creature'),
    )
    HEROES_GROUP = (
           ('HU','Humanoid'),
           ('BP','Big plant'),
           ('DR','Dragon'),
           ('R','Rodent'),
           ('I','Insect'),           
           ('M','Mamal'),
           ('R','Reptile'),           
       ) 
    HEROES_BREED = (
            ('HU','Human'),
            ('AS','Asgardian'),
            ('FG','Frost Giant'),
            ('H','Hamser'),
            ('R','Rat'),
            ('W','Wasp'),
            ('A','Ant'),
            ('M','Mosquito'),   
            ('C','Crocodile'),
            ('S','Snake'), 
            ('D','Dog'),
            ('C','Cat'),      
            ('RD','Red dragon'),
            ('BD','Black dragon'),  
            ('E','Ent'),
            ('T','Treebeard'),    
            ('LI','Lion'),        
        )       
    name = models.CharField(max_length=25, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(choices=HEROES_KINDS, default='Big creature', max_length=2)
    dead = models.BooleanField(default=False)
    date_of_death  = models.DateTimeField(auto_now_add=False, null=True)#, blank=True
    group = models.CharField( choices=HEROES_GROUP, default='Humanoid', max_length=2)
    breed = models.CharField( choices=HEROES_BREED, default='Human', max_length=2)
    
    def kill(self ):
        self.dead = True
        self.date_of_death = datetime.now()
        
    def get_wins_number(self ):
        wining_battles = Battle.objects.filter(winner_id = self.id)
        return wining_battles.count()
        
    def get_defeats_number(self ):
        losing_battles = Battle.objects.filter( Q( Q(fighter1 = self.id) | Q(fighter2 = self.id)) & ~Q(winner_id=self.id))
        return losing_battles.count()
    
    def __str__(self):
        return 'name = %s id = %s' % (self.name, self.id)  

class HeroRank(models.Model):
    hero = models.ForeignKey(Hero, related_name='hero',  null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=25, blank=True, default='')
    wins = models.BigIntegerField(default=0)
    defeats = models.BigIntegerField(default=0)
    #def __init__(self, hero, name, wins):
    def initialize(self, hero, name, wins, defeats):
        self.hero = hero
        self.name = name
        self.wins = wins
        self.defeats = defeats
        
    def __str__(self):
        return 'hero name = %s wins = %s' % (self.hero.name, self.wins) 
    
    class Meta:
        managed = False
        
class DeadHero(models.Model):
    
    hero_id = models.ForeignKey(Hero, related_name='hero_id',  null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=25, blank=True, default='')
    date_of_death  = models.DateTimeField(auto_now_add=False, null=True)
    wins = models.BigIntegerField(default=0)
    
    def initialize(self, dead_hero_id, name, date_of_death, wins):
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
    fighter1 = models.ForeignKey(Hero, related_name='fighter1', on_delete=models.CASCADE) #null=True, on_delete=models.SET_NULL,
    fighter2 = models.ForeignKey(Hero, related_name='fighter2', on_delete=models.CASCADE)
    winner_id = models.ForeignKey(Hero, related_name='winner',  on_delete=models.CASCADE)
    
    def __str__(self):
        return 'id = %s winner = %s' % (self.id, self.winner_id.name)    