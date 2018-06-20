from rest_framework import serializers
from heroes.models import Hero, Battle


#class HeroesSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Hero
        #fields = ('id', 'name', 'created', 'kind', 'dead', 'date_of_dead') 
    
    
class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'created', 'kind', 'group', 'breed', 'dead', 'date_of_dead') 
          
#class FightSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Battle 
        #fields = ('fighter1', 'fighter2', 'winner_id') 

         