from django.urls import path
from .views import *

urlpatterns = [

    path('make_vote/', MakeVoteCountView.as_view(), name='make_vote'),
    path('menu/', GetMenuByRestourantAndCurrentDay.as_view(), name='get_menu'),
    path('get_vote/', GetVoteResults.as_view(), name='get_vote'),
    path('add_restaurant/', MakeRestaurant.as_view(), name='add_restaurant')
    
]
