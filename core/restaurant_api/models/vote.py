

from employees.models import Employee
from django.db import models
from django.shortcuts import get_object_or_404

from .menu import Menu



class VoteCounts(models.Model):
    
    menu = models.ForeignKey(
        to=Menu,
        on_delete=models.CASCADE,
        related_name="Menu",
    )
    user = models.OneToOneField(
        to=Employee,
        on_delete=models.CASCADE,
    )
    date = models.DateField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f'{self.menu} {self.user.username}'


    @classmethod
    def get_vote(self, id) -> list:
        vote = get_object_or_404(VoteCounts, id=id)
        return [vote]
    
    @classmethod
    def get_total_vote(self) -> dict:
        data = {}
        items = ''
        menus = Menu.objects.all()
        for menu in menus:
            count = VoteCounts.objects.filter(menu=menu)
            if count:
                items += (f'{count.first().menu} : {count.count()}, ')
        data['total_vote'] = items
        return data

