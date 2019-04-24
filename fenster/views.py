from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Fenster
from .pss import yapass

def add(request):
    if request.method == "POST":
        f = Fenster(
            fenster_width=request.POST["fenster_width"],
            fenster_height=request.POST["fenster_height"],
            fenster_scheme=request.POST["fenster_scheme"],
            fenster_price=request.POST["fenster_price"]
        )
        f.save()
        return HttpResponseRedirect("/fenster")
    return render(request, 'fenster/add.html')


def index(request):
    return display_all(request)


def buy(request):
    if request.method == "POST":
        if 'selected_fenster' in request.POST:
            f = Fenster.objects.get(
                pk=request.POST['selected_fenster']
            )
            f.for_rent=False
            f.save()
            send_mail(
                subject='Fenster was sold',
                message='Fenster #%i was sold.' % f.id,
                from_email='alisawera@yandex.ru',
                recipient_list=['alisawera@gmail.com'],
                auth_user="alisawera",
                auth_password=yapass
            )

    return HttpResponseRedirect("/fenster")  # relative to 127.0.0.1


def display_all(request, context={}):
    fenster_list = Fenster.objects.filter(for_rent=True).order_by("id")
    context["fenster_list"] = fenster_list
    return render(request, 'fenster/index.html', context)

