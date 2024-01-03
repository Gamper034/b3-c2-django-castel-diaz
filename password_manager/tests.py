from django.test import TestCase
import unittest
from .models import Password


class PasswordTestCase(TestCase):
    
    #Tester si le mot de passe est bien créé
    def setUp(self):
        password = Password.objects.create(name="Test", url="https://test.fr", login="Test", password="password")
    #Tester si le mot de passe est bien créé
    def test_get_password(self):
        test = Password.objects.get(name="Test")
        self.assertEqual(test.name, "Test")
        self.assertEqual(test.url, "https://test.fr")
        self.assertEqual(test.login, "Test")
        self.assertEqual(test.password, "password")

    #Tester si le mot de passe est bien modifié
    def test_update_password(self):
        test = Password.objects.get(name="Test")
        test.name = "Test2"
        test.url = "https://test2.fr"
        test.login = "Test2"
        test.password = "password2"
        test.save()
        self.assertEqual(test.name, "Test2")
        self.assertEqual(test.url, "https://test2.fr")
        self.assertEqual(test.login, "Test2")
        self.assertEqual(test.password, "password2")
    
    #Tester si le mot de passe est bien supprimé
    def test_delete_password(self):
        test = Password.objects.get(name="Test")
        test.delete()
        self.assertEqual(len(Password.objects.all()), 0)
    
    #Tester si le mot de passe est bien récupéré
    def test_get_passwords(self):
        Password.objects.create(name="Test2", url="https://test2.fr", login="Test2", password="password2")
        Password.objects.create(name="Test3", url="https://test3.fr", login="Test3", password="password3")
        self.assertEqual(len(Password.objects.all()), 3)
