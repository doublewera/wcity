from django.shortcuts import render

def index(request):
    context = {
        "window_height": 100,
        "window_width": 50,
        "fenstertypes": [True, True, False, None, ""],
    }
    return render(request, 'fenster/index.html', context)

