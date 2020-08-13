from django.shortcuts import render

from django.db.models import Subquery
from rest_framework import viewsets, status
from rest_framework.response import Response
from food.serializers import RestaurantSerializer, RestaurantDetailSerializer
from food.models import Restaurant, Image
# Create your views here.

class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantDetailSerializer

    def get_queryset(self):
        food_type = self.request.GET.get('type')
        if food_type:
            images = Image.objects.filter(category=food_type)
            if food_type == '0':
                images = images.filter(prob_burger__gt=0.7).order_by('-prob_burger')
            elif food_type == '1':
                images = images.filter(prob_pizza__gt=0.7).order_by('-prob_pizza')
            else:
                images = images.filter(prob_salad__gt=0.7).order_by('-prob_salad')

            return  Restaurant.objects.filter(
                id__in=Subquery(images.values('restaurant_id'))
            ).order_by('id')


        return Restaurant.objects.all().order_by('id')


    def get_serializer(self, *args, **kwargs):
        kwargs['food_type'] = self.request.GET.get('type')
        return super().get_serializer(*args, **kwargs)

    def retrieve(self, request, pk=None):
        try:
            restaurant = self.get_queryset().get(business_id=pk)
            serializer = self.get_serializer(restaurant)

            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

