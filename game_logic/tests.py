from django.test import TestCase, Client
from django.urls import reverse
from game_logic.models import Game
from django.contrib.auth.models import User


class Clue1TestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_correct_combination(self):
        user = User.objects.create(username='testuser')
        game = Game.objects.create(user=user)
        response = self.client.post(reverse('game_logic:clue1'), {
            'hole-A': '1',
            'hole-B': '3',
            'hole-C': '4',
            'hole-D': '2',
            'hole-E': '6',
            'hole-F': '5',
        })
        self.assertEqual(response.status_code, 200)
        game.refresh_from_db()
        self.assertTrue(game.clue_1_completed)
        self.assertIsNotNone(game.clue_1_time)
        self.assertTemplateUsed(response, 'game_logic/clue1.html')
        self.assertContains(response, 'Congratulations!')

    def test_incorrect_combination(self):
        response = self.client.post(reverse('game_logic:clue1'), {
            'hole-A': '1',
            'hole-B': '2',
            'hole-C': '3',
            'hole-D': '4',
            'hole-E': '5',
            'hole-F': '6',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_logic/clue1.html')
        self.assertContains(response, 'Wrong combination')


class Clue2TestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.url = reverse('game_logic:clue2')

    def test_clue2_correct_path(self):
        self.client.login(username=self.username, password=self.password)
        data = {'pathway': 'ACHJ'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'is_correct')
        self.assertTemplateUsed(response, 'game_logic/clue2.html')

        game = Game.objects.get(user=self.user)
        self.assertTrue(game.clue_2_completed)
        self.assertGreater(game.clue_2_time.total_seconds(), 0)

    def test_clue2_incorrect_path(self):
        self.client.login(username=self.username, password=self.password)
        data = {'pathway': 'XYZ'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'is_correct')
        self.assertContains(response, 'You encountered a dead end')

        game = Game.objects.filter(user=self.user).first()
        self.assertIsNone(game.clue_2_completed)
        self.assertIsNone(game.clue_2_time)


class Clue3TestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.url = reverse('game_logic:clue3')

    def test_clue3_correct_decryption(self):
        self.client.login(username=self.username, password=self.password)
        data = {'cipher': 'PIRATE KING'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'is_correct')
        self.assertTemplateUsed(response, 'game_logic/clue3.html')

        game = Game.objects.get(user=self.user)
        self.assertTrue(game.clue_3_completed)
        self.assertGreater(game.clue_3_time.total_seconds(), 0)

    def test_clue3_incorrect_decryption(self):
        self.client.login(username=self.username, password=self.password)
        data = {'cipher': 'ABC'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'is_correct')
        self.assertContains(response, 'You did wrong decryption')

        game = Game.objects.filter(user=self.user).first()
        self.assertIsNone(game.clue_3_completed)
        self.assertIsNone(game.clue_3_time)


class Clue4TestCase(TestCase):
    def test_clue4_correct_move(self):
        user = User.objects.create(username='testuser')
        game = Game.objects.create(user=user)
        data = {
            'piece': 'queen',
            'move': 'e4',
        }
        response = self.client.post(reverse('game_logic:clue4'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_logic/clue4.html')
        self.assertTrue(response.context['is_correct'])
        game.refresh_from_db()
        self.assertTrue(game.clue_4_completed)
        self.assertIsNotNone(game.clue_4_time)

    def test_clue4_incorrect_move(self):
        user = User.objects.create(username='testuser')
        game = Game.objects.create(user=user)
        data = {
            'piece': 'queen',
            'move': 'd3',
        }
        response = self.client.post(reverse('game_logic:clue4'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_logic/clue4.html')
        self.assertFalse(response.context['is_correct'])
        game.refresh_from_db()
        self.assertFalse(game.clue_4_completed)
        self.assertIsNone(game.clue_4_time)


class Clue5TestCase(TestCase):
    def test_clue5_view(self):
        user = User.objects.create(username='testuser')
        game = Game.objects.create(user=user)
        response = self.client.get(reverse('game_logic:clue5'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_logic/clue5.html')
        game.refresh_from_db()
        self.assertTrue(game.clue_5_completed)
        self.assertIsNotNone(game.clue_5_time)
