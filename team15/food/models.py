from django.db import models

# Create your models here.

class Restaurant(models.Model):
	business_id = models.CharField(max_length=64, unique=True);	
	name = models.CharField(max_length=256)
	address = models.CharField(max_length=256)
	postal_code = models.IntegerField()
	is_open = models.BooleanField(default=True)
	hours = models.TextField()	
	latitude = models.FloatField()
	longitude = models.FloatField()
	stars = models.FloatField()
	review_count = models.IntegerField()

	def __str__(self):
		return self.name



class Image(models.Model):
	BURGER = 0
	PIZZA = 1
	SALAD = 2

	CHOICES = [ (BURGER, "Burger"), (PIZZA, "Pizza"), (SALAD,"Salad")] 
	restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name='images')
	image_id = models.CharField(max_length=64)
	category = models.IntegerField(choices=CHOICES)
	prob_burger = models.FloatField()
	prob_pizza = models.FloatField()
	prob_salad = models.FloatField()

