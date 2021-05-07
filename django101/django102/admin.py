from django.contrib import admin

from django102.Models.game import Game
from django102.Models.person import Person
from django102.Models.player import Player

admin.site.register(Game)

admin.site.register(Player)
admin.site.register(Person)