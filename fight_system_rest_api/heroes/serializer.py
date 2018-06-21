from rest_framework import serializers
from heroes.models import Hero, Battle, HeroRank


#class HeroesSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Hero
        #fields = ('id', 'name', 'created', 'kind', 'dead', 'date_of_death') 
    
    
class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'created', 'kind', 'group', 'breed', 'dead', 'date_of_death') 
        
class HeroesSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'created', 'kind', 'group', 'breed' )         
      
#class FightSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Battle 
        #fields = ('fighter1', 'fighter2', 'winner_id') 

class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ('id', 'created', 'fighter1', 'fighter2', 'winner_id' ) 
         
class HeroesRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroRank
        fields = ('id', 'hero_id', 'hero_name','wins', 'defeats') 
