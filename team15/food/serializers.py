from rest_framework import serializers
from food.models import Restaurant, Image



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image_id', 'category', 'prob_burger', 'prob_pizza', 'prob_salad']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['business_id', 'name', 'is_open', 'address', 'postal_code',
                  'latitude','longitude','stars', 'review_count', 'hours']

class RestaurantDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_images')

    def __init__(self, *args, **kwargs):
        try:
            self.food_type = kwargs.pop('food_type')
        except KeyError:
            self.food_type = None

        super().__init__(*args, **kwargs)


    def get_images(self, restaurant):
        food_type = self.food_type
        images = Image.objects.filter(restaurant=restaurant)
        if food_type:
            images = images.filter(category=food_type)
            if food_type == '0':
                images = images.filter(prob_burger__gt=0.7).order_by('-prob_burger')
            elif food_type == '1':
                images = images.filter(prob_pizza__gt=0.7).order_by('-prob_pizza')
            else:
                images = images.filter(prob_salad__gt=0.7).order_by('-prob_salad')
        try:
            images = images[0:1]
        except IndexError:
            images=[]
        serializer = ImageSerializer(images, many=True)
        return serializer.data

    class Meta:
        model = Restaurant
        fields = ['business_id', 'name', 'is_open', 'address', 'postal_code',
                  'latitude', 'longitude', 'stars', 'review_count', 'hours',
                  'images']
