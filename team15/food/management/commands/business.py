from django.core.management.base import BaseCommand
from food.models import Restaurant, Image
import csv

Image.objects.all().delete()
Restaurant.objects.all().delete()

class Command(BaseCommand):
    def handle(self, *args, **options):
        keys = ['business_id', 'name', 'address', 'postal_code', 
    	       'latitude', 'longitude', 'stars', 'review_count', 
    	       'is_open', 'hours']
        with open("business.csv") as fp:
        	reader = csv.DictReader(fp)
        	h = next(reader)
        	
        	for line in reader:
        		d = {}
        		for k in keys:
        			d[k] = line[k]

        		d['postal_code'] = int(float(d['postal_code']))
        		Restaurant.objects.create(**d)