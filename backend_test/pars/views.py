# coding=utf-8
from django.shortcuts import render
from .parser import parse_url
from .models import UrlModel, H1_tag
import  requests
from django.shortcuts import get_object_or_404
from .forms import UrlForm
from django.views.generic.list import ListView

class UrlsListView(ListView):
    model = UrlModel
    template_name = 'home.html'


def parse(request, id):
    message = 'Пока пусто'
    url = get_object_or_404(UrlModel, pk=id)


    try:
        # передаем объекс Url в функцию парсинга функия парсинга
        if request.method == 'POST':
            url = parse_url(url)
            url.save()
            message = 'Сайт успешно пропарсился '

        # requests выбрасывает requests.exceptions.ConnectionError при неправильной передачи адреса сайта

    except requests.exceptions.ConnectionError:
        message = "сайт с таким адресом  не существует либо адрес  введен неправильно"

    tags = '' # здесь будут храниться все теги h1 в виде строки
    for tag in url.h1_tags.all():
        tags = tags + '\n' + (str(tag))

    table1 = url.success

    table2 = '{} - \n {} \n {} \n {}'.format(url.url, url.title, url.charset, tags)
    form = UrlForm({'table1': table1,
                    'table2': table2
                    })

    return render(request,
                  'result.html',
                  {'form': form,
                   'message': message})

