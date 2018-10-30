from django.test import TestCase
from django.contrib.auth.models import User

from . forms import projectForm


class LoginTest(TestCase):
	"""login testcase"""
	
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', email='test@dispostable.com', password='top_secret')

	def test_user_can_login(self):
		response = self.client.post("/login", {"username": "testuser", "password": "top_secret"})


class projectFormTest(TestCase):
	"""project form test case"""

	def test_forms(self):
		form_data = {"name":"test","client":"amazon","budget":"1000","mobile":"9876543210","email":"test@dispostable.com","resource":"10","duration":"1000","target_date":"2018-10-30"}
		form = projectForm(form_data)
		self.assertTrue(form.is_valid())


class viewTest(TestCase):
	"""test view"""

	def test_login_view(self):
		response = self.client.get('/login/')
		self.assertEqual(response.status_code, 200)

	def test_signup_view(self):
		response = self.client.get('/signup/')
		self.assertEqual(response.status_code, 200)
