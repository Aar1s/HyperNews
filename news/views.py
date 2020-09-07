from django.shortcuts import render, HttpResponse
from django.views import View
import itertools, json

with open('C:\\Users\\User\\PycharmProjects\\HyperNews Portal\\task\\hypernews\\news.json', 'r') as json_file:
    dict_from_json = json.load(json_file)


class IntroView(View):
    def get(self, request):
        return HttpResponse('Coming soon')


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'main/Main.html')


class NewsView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'Created': dict_from_json[0]['created'],
            'Title': dict_from_json[0]['title'],
            'Text': dict_from_json[0]['text'],
        }
        return render(request, 'news/news.html', context=context)

