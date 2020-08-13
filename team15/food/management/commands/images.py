from django.core.management.base import BaseCommand
from food.models import Restaurant, Image
import csv

Image.objects.all().delete()
class Command(BaseCommand):
    def handle(self, *args, **options):
        # number,business_id,photo_id,prob_burger,prob_salad,prob_pizza
        keys = ['prob_burger', 'prob_pizza', 'prob_salad']

        with open("images.csv") as fp:
            reader = csv.DictReader(fp)

            for line in reader:
                probs = [line[x] for x in keys]
                category = 2
                m = max(probs)
                if probs[0] == m:
                    category = 0
                elif probs[1] == m:
                    category = 1
                try:
                    r = Restaurant.objects.get(business_id=line['business_id'])
                    Image.objects.create(restaurant=r, image_id=line['photo_id'],
                                         category=category, prob_burger=probs[0],
                                         prob_pizza=probs[1], prob_salad=probs[2])
                except Restaurant.DoesNotExist:
                    #print(line['business_id'])
                   pass
                    #break
