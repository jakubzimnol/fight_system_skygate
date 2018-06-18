from rest_framework import serializers
from heroes.models import Hero


#class HeroesSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Hero
        #fields = ('id', 'name', 'created', 'kind', 'dead', 'date_of_dead') 
    
    
class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'created', 'kind' )#, 'dead', 'date_of_dead') 
        #fields = ('id', 'humanoids', 'big_plants', 'dragons', 'mamals', 'reptiles', 'insects', 'rodents')        

  