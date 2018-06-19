from django.db import models
from datetime import datetime  

   
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
        )       
    name = models.CharField(max_length=25, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(choices=HEROES_KINDS, default='Big creature', max_length=2)
    dead = models.BooleanField(default=False)
    date_of_dead  = models.DateTimeField(auto_now_add=False, null=True)#, blank=True
    group = models.CharField( choices=HEROES_GROUP, default='Humanoid', max_length=2)
    breed = models.CharField( choices=HEROES_BREED, default='Human', max_length=2)
    
    def kill(self ):
        self.dead = True
        self.date_of_dead = datetime.now()
        

class Battle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fighter1 = models.ForeignKey(Hero, related_name='fighter1', on_delete=models.CASCADE)
    fighter2 = models.ForeignKey(Hero, related_name='fighter2', on_delete=models.CASCADE)
    winner_id = models.ForeignKey(Hero, related_name='winner', on_delete=models.CASCADE)