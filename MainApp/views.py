from django.shortcuts import render
from django.shortcuts import HttpResponse

ITEMS = (
    {'id': 1, 'name': 'Фитолакс №40'},
    {'id': 2, 'name': 'Орвис №10 таб'},
    {'id': 3, 'name': 'Товар 3'},
)


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

def items_details(request, id):
    for item in ITEMS:
        if item['id'] == id:
            return HttpResponse(f"""{item['name']}</br>""")


def items(request):
    items_str = "<ul>"
    # <ul>
    #     <li>Товар-1</li>
    #     <li>Товар-1</li>
    #     <li>Товар-1</li>
    # </ul>
    for item in ITEMS:
        items_str += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    items_str += "</ul>"
    return HttpResponse(items_str)