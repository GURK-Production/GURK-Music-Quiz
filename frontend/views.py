from django.shortcuts import render


# Create your views here.

def index(request, *args, **kwargs):
    return render(request, 'frontend/landingPage.html')


def lobby(request, room_name):
    return render(request, 'frontend/lobbyPage.html', {
        "room_name": room_name,
    })


def joinGame(request, room_name):
    return render(request, 'frontend/joinGamePage.html', {
        "room_name": room_name,
    })


def selection(request, room_name):
    return render(request, "frontend/selectionPage.html", {
        "room_name": room_name
    })

def game(request, room_name):
    return render(request, "frontend/gamePage.html", {
        "room_name": room_name
    })
