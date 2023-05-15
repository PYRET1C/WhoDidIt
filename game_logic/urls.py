from django.urls import path
from game_logic import views

# TEMPLATE URLS
app_name = 'game_logic'

urlpatterns = [
    path('game/',views.game,name='game'),
    path('clue1/',views.clue1,name='clue1'),
    path('clue2/',views.clue2,name='clue2'),
    path('clue3/',views.clue3,name='clue3'),
    path('clue4/',views.clue4,name='clue4'),
    path('clue5/',views.clue5,name='clue5'),
    path('solution',views.solution,name='solution'),
    path('deadend1',views.deadend1,name='deadend1'),
    path('deadend2',views.deadend2,name='deadend2'),
]
