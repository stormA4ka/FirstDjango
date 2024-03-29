from django.http import Http404
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import models
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


# ITEMS = (
#     {'id': 1, 'name': 'Фитолакс №40', 'quantity': 5},
#     {'id': 2, 'name': 'Орвис №10 таб', 'quantity': 15},
#     {'id': 3, 'name': 'Товар 3', 'quantity': 0},
# )


def home(request):
    name = "Дергилёв А.В."
    text = f"<h1>Изучаем Django</h1>" \
           f"<strong>Автор</strong>: <i>{name}<i>"
    return HttpResponse(text)


def about(request):
    first_name = 'Алекссандр'
    second_name = 'Дергилёв'
    surname = 'Вячеславович'
    tel = '8-926-726-36-10'
    email = 'stm.87@mail.ru'
    text = f"Имя: <b>{first_name}</b><br>" \
           f"Фамилия: <b>{second_name}</b><br>" \
           f"Отчество: <b>{surname}</b><br>" \
           f"Телефон: <b>{tel}</b><br>" \
           f"e-mail: <b>{email}</b><br>" \

    return HttpResponse(text)

def index(request):
    context = {
        'first_name': 'Александр',
        'second_name': 'Дергилёв'
    }
    return render(request, "index.html")


def items(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)


def item_details(request, id):
    try:
        item = Item.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        "item": item

    }
    return render(request, "item_page.html", context)
