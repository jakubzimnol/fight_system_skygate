from django.test import TestCase
from heroes.models import Hero, Battle

class TestHero(TestCase):
  
  def setUp(self):
    Hero.objects.create(name='Iron man', kind='Big_creature', group='Humanoid', breed='Human')
    Hero.objects.create(name="Simba", kind="Medium_creature", group='Mamal', breed='Lion')
    
  def test_heroes(self):
    lion = Hero.objects.get(name="Simba")
    human = Hero.objects.get(name="Iron man")
    battle = Battle.objects.create(fighter1=lion, fighter2=human, winner_id=lion)
    self.assertEqual(human.get_wins_number(), 0)
    self.assertEqual(lion.get_wins_number(), 1)
    self.assertEqual(human.get_defeats_number(), 1)
    self.assertEqual(lion.get_defeats_number(), 0)
    #self.assertEqual(cat.speak(), 'The cat says "meow"')


#if __name__=="__main__":
#  unittest.main()