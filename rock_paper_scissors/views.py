from django.shortcuts import render
import random

def rock_paper_scissors(request):
    return render(request, 'rock_paper_scissors/rps_game.html')



def rps_result(request):
    choices = ['rock', 'paper', 'scissors']
    comp = random.choice(choices)

    if request.POST.get('rock') == "" and comp == 'paper':
        result = 'You Lose'
    elif request.POST.get('paper') == "" and comp == 'scissors':
        result = 'You Lose'
    elif request.POST.get('scissors') == "" and comp == 'rock':
        result = 'You Lose'
    elif request.POST.get('rock') == "" and comp == 'rock':
        result = 'Its a Draw'
    elif request.POST.get('scissors') == "" and comp == 'scissors':
        result = 'Its a Draw'
    elif request.POST.get('paper') == "" and comp == 'paper':
        result = 'Its a Draw'
    else: result = 'You Win'

    return render(request, 'rock_paper_scissors/result.html', {'result': result, 'comp': comp})

