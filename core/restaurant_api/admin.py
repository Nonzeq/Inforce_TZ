from django.contrib import admin

from .models.menu import Menu
from .models.restaurant import Restaurant
from .models.vote import VoteCounts


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','day', 'restaurant',
                    'desctiptions', 'menu_file', 'date')
    list_display_links = ('id', 'day',)
    search_fields = ('day','title',)


class VoteCountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu','user','date')
    list_display_links = ('id', 'menu', 'date')
    search_fields = ('menu',)


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(VoteCounts, VoteCountsAdmin)
