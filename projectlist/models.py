from django.db import models

# Create your models here.


class projects(models.Model):
	name = models.CharField(max_length=10)
	client=models.CharField(max_length=20)
	budget= models.IntegerField()
	mobile = models.BigIntegerField()
	email = models.EmailField(max_length=254)
	resource = models.IntegerField()
	duration = models.IntegerField()
	status=models.IntegerField(default=1)
	client_details = models.TextField( blank=True)
	target_date= models.DateField()
	created_date=models.DateField(auto_now=True)
	updated_date=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name
