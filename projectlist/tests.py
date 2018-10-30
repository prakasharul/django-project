from django.test import TestCase, Client

# Create your tests here.


from django.contrib.auth.models import User



class LoginTest(TestCase):
	"""login test """
	self.cretendials = {
		'username':'testuser',
		'password':'testpassword'
	}

	self.user = User.objects.create(**cretendials)
	self.client = Client()


	def test_login(self):	
		self.client.login
		response =self.client.post(cretendials, follow=True)

		self.assertTrue(response.context['user'].is_authenticated)