from django.test import TestCase
from heroes.models import Hero

class TestHero(TestCase):
  
  def setUp(self):
    Hero.objects.create(name='Iron man', kind='Big_creature', group='Humanoid', breed='Human')
    Hero.objects.create(name="Simba", kind="Medium_creature", group='Mamal', breed='Lion')

  def test_animals_can_speak(self):
    lion = Animal.objects.get(name="Simba")
    human = Animal.objects.get(name="Iron man")
    #self.assertEqual(lion.speak(), 'The lion says "roar"')
    #self.assertEqual(cat.speak(), 'The cat says "meow"')


#if __name__=="__main__":
#  unittest.main()