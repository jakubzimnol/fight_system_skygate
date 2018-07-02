from rest_framework import serializers
from heroes.models import Hero
from heroes.models import Battle
from heroes.models import HeroRank
from heroes.models import DeadHero
from django.contrib.auth.models import User
    
    
class HeroesSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Hero
        fields = ('id', 'name', 'created', 'kind', 
                  'group', 'breed', 'dead', 'date_of_death',
                  )
        read_only_fields = ('dead', 'date_of_death',)


class HeroesReadOnlySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hero
        fields = ('id', 'name','created', 'kind', 
                  'group', 'breed','dead', 'date_of_death',
                  )       
        read_only_fields = ('id', 'name','created', 'kind', 
                            'group', 'breed','dead', 'date_of_death',
                             )

class BattleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Battle
        fields = ('id', 'created', 'fighter1', 'fighter2', 'winner_id',)
        read_only_fields = ('fighter1', 'fighter2', 'winner_id',)


class BattleReadOnlySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Battle
        fields = ('fighter1', 'fighter2', 'winner_id',)
        read_only_fields = ('fighter1', 'fighter2', 'winner_id',)



class HeroesRankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HeroRank
        fields = ('id', 'hero','name', 'wins', 'defeats',) 


class DeadHeroesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeadHero
        fields = ('hero_id', 'name', 
                  'date_of_death', 'wins',
                  ) 
