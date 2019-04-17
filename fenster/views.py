from django.shortcuts import render

from .models import Fenster
from random import randint

def index(request):
    test_creation()
    fenster_list = Fenster.objects.order_by("id")
    context = {
        "window_height": 100,
        "window_width": fenster_list[0].fenster_width,
        "fenstertypes": [True, False],
        "how_many_fenster": len(fenster_list)
    }
    return render(request, 'fenster/index.html', context)

def test_creation():
# Create a new Fenster.
    f = Fenster(
        fenster_width=randint(100,256),
        window_view=''
    )
    f.save()

