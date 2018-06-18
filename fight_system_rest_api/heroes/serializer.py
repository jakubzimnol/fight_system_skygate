from rest_framework import serializers
from heroes.models import Hero, Big_plant, Humanoid


#class HeroesSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Hero
        #fields = ('id', 'name', 'created', 'kind', 'dead', 'date_of_dead') 
    
    
class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'created', 'kind' )#, 'dead', 'date_of_dead') 
        #fields = ('id', 'humanoids', 'big_plants', 'dragons', 'mamals', 'reptiles', 'insects', 'rodents')        

class SpecialHeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humanoid
        fields = ('id', 'name', 'created', 'kind', 'group', 'breed' )  
        
#class Big_plantSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Big_plant
        #fields = ('id', 'name', 'created', 'kind', 'group', 'breed' )         