from django.test import TestCase
from heroes.models import Hero, Battle, HeroRank
from heroes.services import BattleService

class TestHero(TestCase):

  def setUp(self):
    Hero.objects.create(name='Iron man',
                        kind='Big_creature',
                        group='Humanoid',
                        breed='Human')
    Hero.objects.create(name="Simba",
                        kind="Medium_creature",
                        group='Mamal',
                        breed='Lion')
    self.lion = Hero.objects.get(name="Simba")
    self.human = Hero.objects.get(name="Iron man")
    self.battle = Battle.objects.create(fighter1=self.lion,
                                        fighter2=self.human,
                                        winner_id=self.lion)

  def test_heroes(self):
    self.assertEqual(self.human.get_wins_number(), 0)
    self.assertEqual(self.lion.get_wins_number(), 1)
    self.assertEqual(self.human.get_defeats_number(), 1)
    self.assertEqual(self.lion.get_defeats_number(), 0)


class TestHeroRanking(TestHero):

  def test_heroes_ranking(self):
    hero_rank= HeroRank()
    hero_rank.initialize(self.lion,
                        self.lion.name,
                        self.lion.get_wins_number(),
                        self.lion.get_defeats_number()) 
    hero_rank2= HeroRank()
    hero_rank2.initialize(self.human,
                         self.human.name,
                         self.human.get_wins_number(),
                         self.human.get_defeats_number())

    result = []
    result.append(hero_rank)
    result.append(hero_rank2)
    heroes_testing_rank = BattleService.get_heroes_ranking(Hero.objects.all())
    result = heroes_testing_rank
    self.assertListEqual(heroes_testing_rank, result)


class TestHeroDeads(TestHero):
  
  def test_dead_heroes(self):
    self.lion.kill()
    result = []
    result.append(lion)
    dead_heroes = BattleService.get_dead_heroes(Hero.objects.all())
    self.assertListEqual(dead_heroes, result)


class TestHeroRandomize(TestHero):

  def test_randomize_hero(self):
    randomized_battles = BattleService.random_heroes_for_fight(Hero.objects.all(), Battle.objects.all())
    result_battle = Battle()
    result_battle.fighter1 = self.lion
    result_battle.fighter2 = self.human
    self.assertEqual(randomized_battles, result_battle)