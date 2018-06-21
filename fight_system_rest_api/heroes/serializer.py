from rest_framework import serializers
from heroes.models import Hero, Battle, HeroRank, DeadHero
from django.contrib.auth.models import User

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
        fields = ('id', 'hero','name', 'wins', 'defeats') 

class DeadHeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeadHero
        fields = ('hero_id', 'name', 'date_of_death', 'wins') 


#class DeadHeroesSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)
    #name = serializers.CharField(max_length=25, default='')
    #date_of_deaths = serializers.DateTimeField(required=False, allow_null=True )
    #wins = serializers.IntegerField()
    

    #def create(self, validated_data):
        #"""
        #Create and return a new `Snippet` instance, given the validated data.
        #"""
        #return Snippet.objects.create(**validated_data)

    #def update(self, instance, validated_data):
        #"""
        #Update and return an existing `Snippet` instance, given the validated data.
        #"""
        #instance.id = validated_data.get('id', instance.id)
        #instance.name = validated_data.get('name', instance.name)
        #instance.date_of_deaths = validated_data.get('date_of_deaths', instance.date_of_deaths)
        #instance.wins = validated_data.get('wins', instance.wins)
        #instance.save()
        #return instance    
    
    #class Meta:
        #model = Hero
        #wins = serializers.IntegerField(read_only=True)
        #fields = ('id', 'name', 'wins', 'date_of_death' )
        
class UserSerializer(serializers.ModelSerializer):
    heroes = serializers.PrimaryKeyRelatedField(many=True, queryset=Hero.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')        