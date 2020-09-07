from django.shortcuts import render, HttpResponse, Http404
from django.views import View
import itertools, json


class IntroView(View):
    def get(self, request):
        return HttpResponse('Coming soon')

with open('C:\\Users\\User\\PycharmProjects\\HyperNews Portal\\task\\news.json', 'r') as json_file:
    dict_from_json = json.load(json_file)
groups = []
uniquekeys = []
sorted_data = sorted(dict_from_json, key=lambda i: i['created'][:10], reverse=True)
for k, g in itertools.groupby(sorted_data, lambda i: i['created'][:10]):
    groups.append(list(g))
    uniquekeys.append(k)
print(groups[0][0]['created'])

class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {'groups': groups}
        return render(request,'main/Main.html', context)


class NewsView(View):
    def get(self, request, *args, **kwargs):
        for group in groups:
            for article in group:
                return render(request, 'news/news.html', context={'Text': args})
                if args[0] == article.link:
                    context = {
                        'Created': article.created,
                        'Title': article.title,
                        'Text': article.text,
                    }
                    return render(request, 'news/news.html', context=context)
                else:
                    raise Http404


class CreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'news/create.html')
