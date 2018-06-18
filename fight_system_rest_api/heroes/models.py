from django.db import models
from datetime import datetime  

class fight(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    winner_id = models.ForeignKey(Hero, on_delete=models.CASCADE)
    loser_id = models.ForeignKey(Hero, on_delete=models.CASCADE)
    

class Hero(models.Model):
    HEROES_KINDS = (
        'Big creature',
        'Medium creature',
        'Small creature',
    )
    
    created = models.DateTimeField(auto_now_add=True)
    date_of_dead = models.DateTimeField(auto_now_add=False)
    name = models.CharField(max_length=100, blank=True, default='')
    dead = models.BooleanField(default=False)
    kind = models.CharField(choices=HEROES_KINDS, default='Big creature', max_length=50)
    #list_of_fights = model
    
    def is_dead(self ):
        return self.dead
    
    def kill(self ):
        self.dead = True
        self.date_of_dead = datetime.now()
        
    class Meta:
        abstract = True


class Big_Creatures(Hero):
    HEROES_GROUP = (
        'Humanoid',
        'Big plant',
        'Dragons',
    )    
    group = models.CharField(choices=HEROES_GROUP, default='Humanoid', max_length=50)
    
    class Meta:
        abstract = True
        
    
class Humanoid(Big_Creatures):
    HEROES_BREED = (
        'Human',
        'Asgardian',
        'Frost Giant',
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Human', max_length=50) 
   
class Big_plant(Big_Creatures):
    HEROES_BREED = (
        'Ent',
        'Treebeard',
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Ent', max_length=50)     
    
class Dragons(Big_Creatures):
    HEROES_BREED = (
        'Red dragon',
        'Black dragon',
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Red dragon', max_length=50)         
     
    
class Medium_Creatures(Hero):
    HEROES_GROUP = (
        'Mamal',
        'Reptiles',
    )    
    group = models.CharField(choices=HEROES_GROUP, default='Mamal', max_length=50)    
    class Meta:
        abstract = True 
        
        
class Mamal(Big_Creatures):
    HEROES_BREED = (
        'Dog',
        'Cat',
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Cats', max_length=50)         
 
class Reptiles(Big_Creatures):
    HEROES_BREED = (
        'Crocodile',
        'Snake',
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Crocodile', max_length=50)             
    
    
class Small_Creatures(Hero):
    HEROES_GROUP = (
        'Rodent',
        'Insect',
    )    
    group = models.CharField(choices=HEROES_GROUP, default='Rodent', max_length=50)    
    class Meta:
        abstract = True
        
    
class Rodent(Big_Creatures):
    HEROES_BREED = (
        'Hamser',
        'Rat',
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Hamser', max_length=50)             
        
class Insect(Big_Creatures):
    HEROES_BREED = (
        'Wasp',
        'Ant',
        'Mosquito',
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Hamser', max_length=50)             
                