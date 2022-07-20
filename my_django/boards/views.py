from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Board


def home(request):
    # return HttpResponse('Hello, World!')
    """
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)
    # boards_names = ['Django', 'Python']

    response_html = '<br>'.join(boards_names)  # response_html = 'Django<br>Python'

    return HttpResponse(response_html)
    """

    boards = Board.objects.all()

    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = Board.objects.get(pk)
    return render(request, 'topics.html', {'board': board})
