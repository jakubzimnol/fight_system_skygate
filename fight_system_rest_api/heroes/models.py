from django.db import models
from datetime import datetime  

   

class Hero(models.Model):
    HEROES_KINDS = (
        ('B','Big creature'),
        ('M','Medium creature'),
        ('S','Small creature'),
    )
    name = models.CharField(max_length=25, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(choices=HEROES_KINDS, default='Big creature', max_length=2)
    dead = models.BooleanField(default=False)
    date_of_dead = models.DateTimeField(auto_now_add=False, null=True)#, blank=True
    #list_of_fights = model
    
    def is_dead(self ):
        return self.dead
    
    def kill(self ):
        self.dead = True
        self.date_of_dead = datetime.now()
        
    #class Meta:
     #   abstract = True


class Fight(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    winner_id = models.ForeignKey(Hero, related_name='winner', on_delete=models.CASCADE)
    loser_id = models.ForeignKey(Hero, related_name='looser', on_delete=models.CASCADE)


class Big_Creatures(Hero):
    HEROES_GROUP = (
        ('HU','Humanoid'),
        ('BP','Big plant'),
        ('DR','Dragon'),
    )    
    group = models.CharField(choices=HEROES_GROUP, default='Humanoid', max_length=2)
    
    class Meta:
        abstract = True
        
    
class Humanoid(Big_Creatures):
    HEROES_BREED = (
        ('HU','Human'),
        ('AS','Asgardian'),
        ('FG','Frost Giant'),
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Human', max_length=2) 
   
class Big_plant(Big_Creatures):
    HEROES_BREED = (
        ('E','Ent'),
        ('T','Treebeard'),
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Ent', max_length=2)     
    
class Dragon(Big_Creatures):
    HEROES_BREED = (
        ('RD','Red dragon'),
        ('BD','Black dragon'),
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Red dragon', max_length=2)         
     
    
class Medium_Creatures(Hero):
    HEROES_GROUP = (
        ('M','Mamal'),
        ('R','Reptile'),
    )    
    group = models.CharField(choices=HEROES_GROUP, default='Mamal', max_length=2)    
    class Meta:
        abstract = True 
        
        
class Mamal(Big_Creatures):
    HEROES_BREED = (
        ('D','Dog'),
        ('C','Cat'),
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Cats', max_length=2)         
 
class Reptile(Big_Creatures):
    HEROES_BREED = (
        ('C','Crocodile'),
        ('S','Snake'),
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Crocodile', max_length=2)             
    
    
class Small_Creatures(Hero):
    HEROES_GROUP = (
        ('R','Rodent'),
        ('I','Insect'),
    )    
    group = models.CharField(choices=HEROES_GROUP, default='Rodent', max_length=2)    
    class Meta:
        abstract = True
        
    
class Rodent(Big_Creatures):
    HEROES_BREED = (
        ('H','Hamser'),
        ('R','Rat'),
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Hamser', max_length=2)             
        
class Insect(Big_Creatures):
    HEROES_BREED = (
        ('W','Wasp'),
        ('A','Ant'),
        ('M','Mosquito'),
    )   
    breed = models.CharField(choices=HEROES_BREED, default='Wasp', max_length=2)             
                

#class Heroes(models.Model):
    #humanoids = OneToOneField(Humanoid, on_delete=models.CASCADE )
    #big_plants = OneToOneField(Big_plant, on_delete=models.CASCADE )
    #dragons = OneToOneField(Dragon, on_delete=models.CASCADE )
    #mamals = OneToOneField(Mamal, on_delete=models.CASCADE )
    #reptiles = OneToOneField(Reptile, on_delete=models.CASCADE )
    #insects = OneToOneField(Insect, on_delete=models.CASCADE )
    #rodents = OneToOneField(Rodent, on_delete=models.CASCADE )