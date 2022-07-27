
from django.db import models
from .restaurant import Restaurant


class Days(models.TextChoices):
    MONDAY = "MONDAY", "Monday"
    TUESDAY = "TUESDAY", "Tuesday"
    WEDNESDAY = "WEDNESDAY", "Wednesday"
    THURSDAY = "THURSDAY", "Thursday"
    FRIDAY = "FRIDAY", "Friday"
    SATURDAY = "SATURDAY", "Saturday"
    SUNDAY = "SUNDAY", "Sunday"


class Menu(models.Model):
    title = models.CharField(max_length=75, verbose_name="Title of menu")
    day = models.CharField(
        max_length=75, choices=Days.choices, verbose_name="Day")
    restaurant = models.ForeignKey(
        to=Restaurant,
        related_name="restaurant",
        verbose_name="Restaurant",
        on_delete=models.CASCADE,
    )
    desctiptions = models.TextField(verbose_name="Menu")
    menu_file = models.FileField(
        upload_to=f"menus/%d")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Menu")
        verbose_name_plural = ("Menus")

    def __str__(self) -> str:
        return f'{self.restaurant} {self.title}'

    @classmethod
    def get_menu_by_day_and_restaurant(self, day, restaurant):
        menu = Menu.objects.filter(day=day, restaurant=restaurant)
        return menu
