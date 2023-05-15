from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Game
from datetime import timedelta



@login_required
def clue1(request):
    if request.method == 'POST':
        optionA = request.POST.get('hole-A')
        optionB = request.POST.get('hole-B')
        optionC = request.POST.get('hole-C')
        optionD = request.POST.get('hole-D')
        optionE = request.POST.get('hole-E')
        optionF = request.POST.get('hole-F')
        is_correct = False
        if (optionA == '1' and optionB == '3' and optionC == '4' and optionD == '2' and optionE == '6' and optionF == '5'):
            is_correct = True
            user = request.user
            game = Game.objects.filter(user=user).first()

            if game is None:
                game = Game.objects.create(user=user)

            clue1_time = timezone.now() - game.created_at
            game.clue_1_time = clue1_time
            game.clue_1_completed = True
            game.save()
            context = {'is_correct': is_correct}
            return render(request, 'game_logic/clue1.html', context)
        else:
            message = "Wrong combination of the puzzle. Please try again."
            return render(request, 'game_logic/clue1.html', {'message': message})

    return render(request, 'game_logic/clue1.html')


@login_required
def clue2(request):
    if request.method == 'POST':
        str = request.POST.get('pathway').upper()
        is_correct = False
        if str == "ACHJ" or "AFJ":
            is_correct = True
            user = request.user
            game = Game.objects.filter(user=user).first()

            if game is None:
                game = Game.objects.create(user=user)

            clue2_time = timezone.now() - game.created_at-game.clue_1_time
            game.clue_2_time = clue2_time
            game.clue_2_completed = True
            game.save()
            return render(request, 'game_logic/clue2.html', {'is_correct': is_correct})
        else:
            message = "You encountered a dead end, try again with a different path."
            return render(request, 'game_logic/clue2.html', {'message': message})

    return render(request, 'game_logic/clue2.html')


@login_required
def clue3(request):
    if request.method == 'POST':
        str = request.POST.get('cipher').upper()
        is_correct = False
        if str == 'PIRATE KING':
            is_correct = True
            user = request.user
            game = Game.objects.filter(user=user).first()

            if game is None:
                game = Game.objects.create(user=user)

            clue3_time = timezone.now() - game.created_at-game.clue_1_time-game.clue_2_time
            game.clue_3_time = clue3_time
            game.clue_3_completed = True
            game.save()
            return render(request, 'game_logic/clue3.html', {'is_correct': is_correct})
        else:
            message = "You did wrong decryption let someone else try it!!"
            return render(request, 'game_logic/clue3.html', {'message': message})
    return render(request, 'game_logic/clue3.html')


@login_required
def clue4(request):
    if request.method == 'POST':
        str = request.POST.get('piece')
        move = request.POST.get('move').lower()
        is_correct = False
        if str == 'queen' and move == 'e4':
            is_correct = True
            user = request.user
            game = Game.objects.filter(user=user).first()

            if game is None:
                game = Game.objects.create(user=user)

            clue4_time = timezone.now() - game.created_at-game.clue_1_time-game.clue_2_time-game.clue_3_time
            game.clue_4_time = clue4_time
            game.clue_4_completed = True
            game.save()
            return render(request, 'game_logic/clue4.html', {'is_correct': is_correct})
        else:
            message = "Your chess skills need improvement. Try again!!"
            return render(request, 'game_logic/clue4.html', {'message': message})
    return render(request, 'game_logic/clue4.html')


@login_required
def clue5(request):
    user = request.user
    game = Game.objects.filter(user=user).first()

    if game is None:
        game = Game.objects.create(user=user)

    clue5_time = timezone.now() - game.created_at-game.clue_1_time-game.clue_2_time-game.clue_3_time-game.clue_4_time
    game.clue_5_time = clue5_time
    game.clue_5_completed = True
    game.save()    
    return render(request, 'game_logic/clue5.html')


@login_required
def solution(request):
    user = request.user
    game = Game.objects.filter(user=user).first()

    if game is None:
        game = Game.objects.create(user=user)

    game.time_taken = (game.clue_1_time or timedelta()) +(game.clue_2_time or timedelta()) +(game.clue_3_time or timedelta()) +(game.clue_4_time or timedelta()) +(game.clue_5_time or timedelta()) +(game.deadend_1_time or timedelta())+(game.deadend_2_time or timedelta())
    game.completed = True
    game.save()   
    context ={'total_time':game.time_taken}
    return render(request, 'game_logic/solution.html',context)


@login_required
def deadend1(request):
    first_time = False
    user = request.user
    game = Game.objects.filter(user=user).first()

    if game is None:
        game = Game.objects.create(user=user)

    deadend1_time = timezone.now() - game.created_at-game.clue_1_time
    game.deadend_1_time = deadend1_time
    game.save()   
    if request.method == 'POST':
        first_time = True
        message = "This is not the right answer. Please try again."
        return render(request, 'game_logic/deadend1.html', {'message': message, 'first_time': first_time})
    return render(request, 'game_logic/deadend1.html')


@login_required
def deadend2(request):
    user = request.user
    game = Game.objects.filter(user=user).first()

    if game is None:
        game = Game.objects.create(user=user)

    deadend2_time = timezone.now() - game.created_at-game.clue_1_time-game.clue_2_time-game.clue_3_time-game.clue_4_time-game.clue_5_time
    game.deadend_2_time = deadend2_time
    game.save()   
    return render(request, 'game_logic/deadend2.html')


@login_required
def game(request):
    # get the current user's game instance or create a new one if it doesn't exist
    game, created = Game.objects.get_or_create(user=request.user)

    context = {
        'game': game,
    }
    return render(request, 'game_logic/clue1.html', context)
