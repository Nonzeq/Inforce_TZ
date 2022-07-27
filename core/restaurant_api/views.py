
import datetime

from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from .services.get_day import getDay

from .serializers.restaurant_serializer import RestaurantSerializer
from .serializers.menu_serializer import MenuSerializer
from .serializers.vote_count_serializer import VoteCountSerializer, VoteSerializer

from .models.vote import VoteCounts
from .models.menu import Menu


class MakeRestaurant(generics.CreateAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated,)

class MakeVoteCountView(generics.ListCreateAPIView):
    serializer_class = VoteCountSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        vote = self.request.query_params.get('menu')
        queryset = VoteCounts.get_vote(vote)
        if queryset:
            VoteCounts.make_vote(vote)
            return queryset


class GetMenuByRestourantAndCurrentDay(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        restaurant = self.request.query_params.get('restaurant')
        queryset = Menu.get_menu_by_day_and_restaurant(
            day=getDay(datetime.datetime.today().strftime('%Y-%m-%d')),
            restaurant=restaurant
        )
        if restaurant is not None:
            return queryset
        return queryset


class GetVoteResults(generics.ListAPIView):
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        count = VoteCounts.get_total_vote()
        if count:
            return [count]
        return []
